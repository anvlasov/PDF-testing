from glob import glob
from string import Template


if __name__ == '__main__':
    with open('index.template.html', 'r') as f:
        template = Template(f.read())

    insertion = ''
    if files := glob('*.pdf'):
        insertion += '<h2>PDF files:</h2>'
        for file in files:
            insertion += f'\n      <a href="pdfs/{file}">{file}</a><br>'
    if files := glob('large/*.pdf'):
        insertion += '\n      <h2>Large PDF files:</h2>'
        for file in files:
            name = file.split('/')[-1]
            insertion += f'\n      <a href="pdfs/large/{name}">{name}</a><br>'

    with open('index.html', 'w') as f:
        f.write(template.substitute({'FILES': insertion}))
