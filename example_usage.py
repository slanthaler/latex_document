from latex_document import LatexDocument

title = 'Numerical Experiment Visualization'
author = 'John Doe'

doc = LatexDocument(title, author)

doc.add_section('A simple example')
doc.add_subsection('About')
doc.add_text('This document illustrates the use of the \\texttt{LatexDocument} python class. The intent is to have a simple way to take a list of files \\texttt{file\\_list}, with each file containing a plot, and arrange them in a latex document.')

doc.add_subsection('Let''s plot a list')
file_list = [
    'example-image-a',
    'example-image-b',
    'example-image-c',
    'example-image'
    ]
doc.add_figure(file_list)

doc.add_subsection('Let''s plot including captions')
file_list = [
    'example-image-a',
    'example-image-b',
    'example-image-c',
    'example-image'
    ]
caption_list = [
    'example A',
    'example B',
    'example C',
    'example'
    ]
doc.add_figure(file_list, caption_list)

doc.add_subsection('More possibilities')
doc.add_text('We can also change the number of columns (e.g. 3 columns):')
file_list = [
    'example-image-a',
    'example-image-b',
    'example-image-c',
    'example-image'
    ]
caption_list = [
    'example A',
    'example B',
    'example C',
    'example'
    ]
doc.add_figure(file_list, caption_list, columns=3)

doc.add_text('Or we can choose to fill the plot up column-by-column, rather than row-by-row. Here with 3 columns')
file_list = [
    'example-image-a',
    'example-image-b',
    'example-image-c',
    'example-image'
    ]
caption_list = [
    'example A',
    'example B',
    'example C',
    'example'
    ]
doc.add_figure(file_list, caption_list, columns=3, row_first=False)

doc.add_text('And a final example with just 1 column.')
file_list = [
    'example-image-a',
    'example-image-b',
    'example-image-c',
    'example-image'
    ]
caption_list = [
    'example A',
    'example B',
    'example C',
    'example'
    ]
doc.add_figure(file_list, caption_list, columns=1, row_first=False, scaling=.3)

doc.add_section('Closing')
doc.add_text('In closing, the \\texttt{LatexDocument} class allows us to easily generate a pdf with hundreds of plots, helping to visualize numerical experiments, which often involve scaling over a number of parameters.')

filename = 'example.tex'
doc.write(filename)
doc.compile()
