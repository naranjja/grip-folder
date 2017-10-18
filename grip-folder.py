from os import listdir
from os.path import isdir
from sys import argv
from subprocess import check_call
from re import sub


def change_relative_links(path, html_file):
    with open(path + html_file, 'r') as f:
        html = f.read()  # read the HTML content
        html = sub(r'\/([a-zA-Z0-9-\/]+)\.md', r'\1.html', html)  # make Markdown references relative and point to HTML file
        html = html.replace('"..', '"../')  # fix jumping relative paths
        html = html.replace('href="/', 'href="')  # remove other relative references
        html = html.replace('src="/', 'src="')  # remove other relative sources

    with open(path + html_file, 'w') as f:
        f.write(html)  # write the new HTML content


def convert_markdown(path, md_file):
    if check_call(['grip', path + md_file, '--export']) == 0:
        change_relative_links(path, md_file.replace('.md', '.html'))


def find_markdown_files(path):
    path += '/'  # failsafe
    for el in listdir(path):  # list all elements in path
        if el not in ignored:  # if the element is not ignored
            if isdir(path + el):  # if element is a folder
                find_markdown_files(path + el)
            elif el.endswith('.md'):  # else if element is a Markdown file
                convert_markdown(path, el)


if __name__ == '__main__':
    path = argv[1]  # get the first argument as the path
    ignored = ['.git']  # ignore the following folders and file names

    find_markdown_files(path)
