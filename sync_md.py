#!/usr/bin/env python3
import os
import sys
import re
import logging
import argparse
import subprocess

GIT_ROOT = '/home/lyy/331G/code/pics' # gitee图床本地路径
REMOTE_PREFIX='https://gitee.com/lyyiangang/pics/raw/master/' # gitee网址

REG_TXT = r'\!\[.*\]\(imgs/(.*)\)'
logging.basicConfig(level= logging.INFO)
lg = logging.getLogger(__name__)

def replace_with_remote_url(local_path):
    return '![]({})'.format(REMOTE_PREFIX + local_path)

def main():
    lg.info('usage: python sync.py you_markdown_file.md')
    assert(len(sys.argv) == 2)
    m_file = sys.argv[1]
    print('processing {}'.format(m_file))
    with open(m_file, 'r') as fid:
        old_txt = fid.read()
    md_root_dir = os.path.dirname(os.path.abspath(m_file)) 
    # modify markdown first
    final_str = re.sub(REG_TXT, replace_with_remote_url(r'\1') , old_txt)
    final_output_file = '/tmp/tmp.md'
    print('writing to {}'.format(final_output_file))
    with open(final_output_file, 'w') as fid:
        fid.write(final_str)
    match_objs = re.findall(REG_TXT, old_txt)
    
    import shutil
    if match_objs:
        for item in match_objs:
            source_file = os.path.join(md_root_dir, 'imgs/' + item)
            lg.info('copying {} to {}'.format(source_file, GIT_ROOT))
            shutil.copy2(source_file, GIT_ROOT)
    else:
        lg.warn(f'do not match any file, skip sync')
    git_cmd = 'git -C {} '.format(GIT_ROOT)
    out = subprocess.check_output('{} status && {} add . && {} commit -m "sync" && {} push origin master'.format(git_cmd, git_cmd, git_cmd, git_cmd), shell= True)
    lg.info(out.decode('utf-8'))

if __name__ == '__main__':
    main()