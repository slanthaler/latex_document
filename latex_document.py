import math, os

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def list2array(list, columns, row_first, fill=None):
    '''
    convert list to array
    '''
    rows = math.ceil( len(list) / columns )
    list += (rows*columns - len(list)) * [fill]
    array = []
    ind = 0
    if row_first==False:
        rows,columns = columns,rows
    #
    for row in range(rows):
        array.append([])
        for col in range(columns):
            array[row].append(list[ind])
            ind += 1
    #
    if row_first==False:
        array = transpose(array)
    return array
    

class LatexDocument:
    '''
    A class to generate latex documents containing many plots.
    '''
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.filename = None
        self.txt = ''
        self.add_preamble()

    def __str__(self):
        return self.txt
    
    def write(self, filename):
        assert filename[-4:] == '.tex', 'Filename must end in .tex'
        self.filename = filename
        #
        txt = self.txt
        txt += '\n\end{document}\n'

        with open(filename,'w') as f:
            f.write(txt)

    def compile(self):
        os.system('pdflatex ' + self.filename)

    def add_preamble(self):
        preamble = '''
\\documentclass[11pt]{article}

\\usepackage{graphicx}
\\usepackage{subcaption}
\\usepackage{float}

\\title{''' + self.title + '''}
\\author{''' + self.author + '''}

\\begin{document}
\\maketitle
'''
        self.txt += preamble

    def add_text(self, text):
        self.txt += text + '\n\n'
    
    def add_section(self, title):
        self.txt += '\n\\section{' + title + '}\n\n'

    def add_subsection(self, title):
        self.txt += '\n\\subsection{' + title + '}\n\n'
    
    def add_linebreak(self):
        self.txt += '\n\n'

    def add_figure(self, file_list, caption_list=None,
                   caption=None, columns=2, row_first=True, scaling=None):
        '''
        This will take the list of files (each file is a plot), and generate a latex snipped
        consisting of a figure with subfigures arranged in specified number of columns.
    
        If row_first==True, the figures are arranged to fill row-by-row.
        Otherwise, the figures will be filled column-by-column.
        '''
        if caption_list is None:
            caption_list = len(file_list)*[None]
        #
        file_array = list2array(file_list, columns, row_first, fill='')
        caption_array = list2array(caption_list, columns, row_first, fill=None)
        rows = len(file_array)
        cols = columns
        width = (1 / cols) - 0.01
        if scaling is not None:
            width *= scaling
        width = f'{width:0.3f}'
        # 
        self.txt += '\\begin{figure}[H]\n'
        self.txt += '\centering\n' # center all subfigures
        for row in range(rows):
            for col in range(cols):
                file = file_array[row][col]
                cap = caption_array[row][col]
                self.add_subfigure_(file, width, caption=cap)
            self.add_linebreak()
        if caption is not None:
            self.txt += f'\\caption{{{caption}}}\n'
        self.txt += '\\end{figure}\n\n'

    def add_subfigure_(self, filename, width, caption=None):
        if caption is None:
            caption_txt = ''
        else:
            caption_txt = f'    \\caption{{{caption}}}\n'
        includegraphics_txt = f'    \\includegraphics[width=\\textwidth]{{{filename}}}\n'
        if not filename:
            includegraphics_txt = '%' + includegraphics_txt
        #
        self.txt += f'%\n\\begin{{subfigure}}{{{width}\\textwidth}}\n'
        self.txt += includegraphics_txt
        self.txt += caption_txt
        self.txt += '\\end{subfigure}\n'
