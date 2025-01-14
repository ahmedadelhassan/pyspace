# -*- coding: utf-8 -*-
#
# aBRI documentation build configuration file, created by
# sphinx-quickstart on Fri Jan 30 13:24:06 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, inspect

# Add root of the tree --> go to place before docs
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if not root_dir in sys.path:
    sys.path.append(root_dir)

import pySPACE
try:
    pySPACE.load_configuration("config.yaml")
except:
    pass
import pySPACE.missions.nodes

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# autodoc is an extension to extract documentation automatically
# viewcode is an extension to link the corresponding sourcecode
# as a link automatically with syntax highlighting
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx',
              'sphinx.ext.inheritance_diagram',
              'sphinx.ext.graphviz',
              'sphinx.ext.todo',
              'sphinx.ext.pngmath',
              'sphinx.ext.autosummary',
#              'numpy_ext.numpydoc',
#              'matplotlib.sphinxext.plot_directive',
#              'matplotlib.sphinxext.only_directives',
              ]

autosummary_generate = True

# switches the showing of todos on or of
#todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pySPACE'
copyright = u'2014, pySPACE Developer Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.2'
# The full version, including alpha/beta/rc tags.
release = '1.2 release'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['.build', 'templates', 'includes']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Variable for the settings of autodoc
# 'members' of the module or class used with autodoc will we shown
# So the classes don't have to be listed individually when using autodoc with a file module
# 'undoc-members' makes sure, even undocumented members are listed
# 'show-inheritance' adds a short line where you get to know what the mother class is.
# 'private-members' is only available since version 1.1 of sphinx
# Now also 'members' beginning with "_" will be included in documentation.
# 'inherited-members' would also include inherited members in the documentation generation.
# Normally they are ommited because the class doesn't change these functions.
# If you set one of these flags in this configuration value,
# you can use a negated form, 'no-flag', in an autodoc directive, to disable it once.
# .. automodule:: foo
#    :no-undoc-members:

# undoc-members','inherited-members','members','show-inheritance', 'private-members'
# Python “special” members (that is, those named like __special__) will be included if the special-members flag option is given
autodoc_default_flags = ['members','show-inheritance','undoc-members','private-members', 'special-members']
# 'private-members' is only available since version 1.1 of sphinx
# Now also 'members' beginning with "_" will be included in documentation.


# # Activate this parameter to say where its documentation comes from
# # The default 'should be' to concatenate the doc-strings of the class and its
# # __init__ function.
# autoclass_content = 'class' #'both', 'class', 'init'
autoclass_content = 'class' #'both'

# # This value selects if automatically documented members 
# # are sorted alphabetical (value 'alphabetical'), 
# # by member type (value 'groupwise') or by source order (value 'bysource'). 
autodoc_member_order = 'bysource'

# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_theme = "sphinxdoc"
#html_theme_options = {
#    "rightsidebar": "false",
#    "relbarbgcolor": "black"
#}

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'pySPACE.css'


# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "pySPACE documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "graphics/pyspace-logo_small.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "graphics/pyspace-logo.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'docs'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', 'pySPACE.tex', ur'pySPACE Documentation',
   ur'pySPACE Developer Team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "graphics/pyspace-logo_small.png"

# For "manual" documents, if this is true, then top level headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

def fix_sig(app, what, name, obj, options, signature,
                              return_annotation):
    """ Underline class name and separate it from parameters 
    
    **Deprecated**
    """
    if 'class' == what:
        # underline class name manually
        new_signature="\n"
        new_signature+="-"*(len(str(name))+7) # 'class ' is not included in length
        new_signature+="\n"
        if signature:
            # delete beginning and ending brackets
            parameters = signature #[1:-1]
            parameters = parameters.replace(", **kwargs","")
            parameters = parameters.replace(", *args","")
            if len(parameters)>0:
                # add the parameters separately
                # unfortunately this is done in bold for unknown reasons
                # (probably the first newline is the reason)
                # extra dot is added for extra blank line
                new_signature+=".\n"
                new_signature+="Parameters:"
                new_signature+="\n\n"
                # the parameters should be indented but this doesn't work
                new_signature+="        "
                new_signature+=parameters
        return (new_signature, return_annotation)
    else:
        return (signature, return_annotation)

def missing_docstring(app, what, name, obj, options, lines):
    """ Construct a list of components having no docsting 
    
    .. todo:: Discover where the 'type ERROR' comes from in CCS
    """
    if len(lines)==0 and not str(name).endswith("__init__"):
        f = open(os.path.join(os.path.dirname(__file__),".build","html","undocumented.txt"),"a")
        f.write(str(name)+"\n")
    else:
        for line in lines:
            if "document" in line and "todo" in line:
                f = open(os.path.join(os.path.dirname(__file__),".build","html","undocumented.txt"),"a")
                f.write("\n"+str(name)+"\n"+line+"\n \n")

    if 'class' == what and str(name).endswith("Node"):
        # e.g. pySPACE.missions.nodes.spatial_filtering.spatial_filtering.SpatialFilteringNode
        lines.append("")
        lines.append("")
        lines.append(":POSSIBLE NODE NAMES:")
        lines.append("")
        for key, value in pySPACE.missions.nodes.NODE_MAPPING.items():
            if value.__module__+"."+value.__name__==name:
                lines.append("    - **"+key+"**")
        lines.append("")
        lines.append("")

        # also add the possible inputs to the documentation
        lines.append("")
        lines.append("")
        lines.append(":POSSIBLE INPUT TYPES:")
        lines.append("")
        for key, value in pySPACE.missions.nodes.NODE_MAPPING.items():
            if value.__module__+"."+value.__name__==name:
                for input_type in value.get_input_types():
                    lines.append("    - **"+input_type+"**")
                break
        lines.append("")
        lines.append("")


    # Add class summary
    # For unknown reasons, this part produces warnings and errors
    # referring to except and types, but the reason is unclear
    if 'class' == what and not len(lines)==0 and not "Metaclass" in name and \
      not name.endswith("SklearnNode"):
        new_lines=[]
        new_lines.append("")
        new_lines.append("**Class Components Summary**")
        new_lines.append("")
        new_lines.append(".. autosummary::")
        new_lines.append("")
        method_list = inspect.getmembers(obj) #,inspect.ismethod
        for method,value in method_list:
            if not method in ["__doc__","__module__","__metaclass__","__dict__","__init__","__weakref__"] and method in obj.__dict__.keys():
                new_lines.append("    "+method)
#                if "type" in obj.__name__ or "type" in method or "except" in new_lines[-1]:
#                    print obj
#                    print name
#                    print method
#                    print
        # only one method found
        if len(new_lines)<=5:
            new_lines=[]
        lines.extend(new_lines)
        lines.append("")
        lines.append("")


def setup(app):
    """ Activate fix_sig and missing_docstring and delete old 'undocumented.txt'
    
    .. todo:: Fix file handling. Only works with 'make html_complete'
    """
#    app.connect('autodoc-process-signature', fix_sig)
    app.connect('autodoc-process-docstring', missing_docstring)
    # clean up auto-un-documentation files
    fname = os.path.join(os.path.dirname(__file__), ".build", "html",
                         "undocumented.txt")
    if os.access(fname, os.F_OK):
        os.remove(fname)

######################### preparation #########################################

# delete old list of nodes
fname = os.path.join(os.path.dirname(__file__), "nodes.rst")
if os.access(fname, os.F_OK):
    os.remove(fname)

location = "pySPACE.missions.nodes"
offset = len(location) + 1
node_list = []
for key, value in pySPACE.missions.nodes.DEFAULT_NODE_MAPPING.items():
    node_list.append(value.__module__ + "." + value.__name__)
node_list.sort()

######################### header ###############################################

f = open(fname, "a")
f.write(".. AUTO-GENERATED FILE -- DO NOT EDIT! (conf.py)\n")
f.write(".. _node_list: \n")
f.write("\n")
f.write("List of all Nodes \n")
f.write("======================= \n")
f.write("\n")
n = len(node_list)
f.write("pySPACE comes along with a big choice of %d processing nodes.\n" % n)
f.write("This includes numerous wrappers around optional external libraries.\n")
f.write("They can be accessed via the "
    ":class:`~pySPACE.missions.operations.node_chain.NodeChainOperation`.\n")
f.write("In the following you can get an overview on their functionality, \n")
f.write("the mapping from node names in specification files \n")
f.write("to the node class and vice versa.\n")
f.write("\n")
f.write("For details on the usage of the nodes and for getting usage examples, "
        "have a look at their documentation.\n")

######################### node summary #########################################

f.write("\n")
f.write("Mapping of Class Names to Functionality \n")
f.write("--------------------------------------- \n")
f.write("\n")
#f.write("\n.. currentmodule:: %s\n\n"%location)
#f.write(".. autosummary:: \n")
#f.write("    :nosignatures:\n")
#f.write("    :toctree: nodes\n")
f.write("\n")
current_location = ""
for node in node_list:
    if not node == "pySPACE.missions.nodes.base_node.BaseNode" and \
       not "template" in node:
        new_location = node[offset:].split(".")[0]
        # write heading for node subcategory description
        if not new_location == current_location:
            current_module = location + "." + new_location
            f.write("\n")
            f.write("%s\n" % new_location)
            f.write("+" * (len(new_location)) + "\n")
            f.write(" \n|\n\n")
            f.write(".. currentmodule:: %s\n" % location)
            f.write(".. autosummary:: \n\n    %s\n\n|\n\n"
                    % current_module[offset:])
            # if not current_module=="pySPACE.missions.nodes.splitter":
            #     f.write(".. automodule:: %s\n    :no-members:\n\n"%current_module)
            # else:
            #     f.write("Control how data is split into training and testing data\n\n")
            f.write(".. currentmodule:: %s\n" % current_module)
            f.write(".. autosummary:: \n")
            f.write("    :nosignatures:\n")
            f.write("\n")
            current_location = new_location

        current_offset = len(current_module) + 1
        f.write("    " + node[current_offset:] + "\n")
f.write("\n")

######################### new name mapping list ###############################

node_name_dict = pySPACE.missions.nodes.NODE_MAPPING
name_list = [(name, value.__module__[offset:] + "." + value.__name__)
             for name, value in node_name_dict.items()]

######################### node name --> class name ############################

f.write(".. currentmodule:: %s\n\n" % location)

f.write("Mapping of Node Names to Class Names \n")
f.write("------------------------------------ \n")
f.write("\n")
name_list.sort(key=lambda x: x[0].lower())
for name,class_name in name_list:
    f.write("    - " + name + ": " + ":class:`" + class_name + "`" + "\n")

######################### class name --> node name ############################

f.write("\n")
f.write("Mapping of Class Names to Node Names \n")
f.write("------------------------------------ \n")
f.write("\n")
name_list.sort(key=lambda x: (x[1].lower(), x[0]))
for name, class_name in name_list:
    f.write("    - " + ":class:`" + class_name + "`" + ": " + name + "\n")

######################### class name --> example ##############################

# f.write("\n")
# f.write("Mapping of Class Names to Example Dictionary \n")
# f.write("-------------------------------------------- \n")
# f.write("\n")
# name_list.sort(key=lambda x: (x[1].lower(), x[0]))
# for name, class_name in name_list:
#     f.write("    - " + ":class:`" + class_name + "`" + ": " + name + "\n")
f.close()

######################### operation example list #############################

#examples operations
fname=os.path.join(os.path.dirname(__file__),"examples","operations.rst")
if os.access(fname,os.F_OK):
    os.remove(fname)

specs_path=os.path.join(os.path.dirname(__file__),"examples","specs")

examples=os.path.join(specs_path,"operations","examples")

f=open(fname,"a")
       
f.write(".. _operation_examples: \n")
f.write("\n")
f.write("Operation Examples \n")
f.write("=========================== \n")
f.write("\n")
f.write("These are examples of yaml files you can use as a template\n")
f.write("for your own operations. For details on operations have a look at the respective documentation.\n")
f.write("\n")
# adding example files
for folder, _, files in os.walk(examples):
    for fname in files:
        f.write(fname + "\n")
        f.write("------------------------------------------\n")
        f.write("\n")
        f.write(".. literalinclude:: " + os.path.join("specs","operations","examples",fname) + "\n")
        f.write("\t" + ":language: yaml" + "\n")
        f.write("\n")
f.close()

######################### operation chain example list ########################

#examples operation_chains
examples=os.path.join(specs_path,"operation_chains","examples")

fname=os.path.join(os.path.dirname(__file__),"examples","operation_chains.rst")
if os.access(fname,os.F_OK):
    os.remove(fname)

f=open(fname,"a")
       
f.write(".. _operation_chain_examples: \n")
f.write("\n")
f.write("Operation Chain Examples \n")
f.write("============================ \n")
f.write("\n")
f.write("These are examples of yaml files you can use as a template\n")
f.write("for your own operation chains. For details on operation chains have a look at the respective documentation.\n")
f.write("\n")
# adding example files
for folder, _, files in os.walk(examples):
    for fname in files:
        f.write(fname + "\n")
        f.write("------------------------------------------\n")
        f.write("\n")
        f.write(".. literalinclude:: " + os.path.join("specs","operation_chains","examples",fname) + "\n")
        f.write("\t" + ":language: yaml" + "\n")
        f.write("\n")
f.close()

######################### preparation of external node documentation ##########

# delete old list of nodes
fname=os.path.join(os.path.dirname(__file__),"external_nodes.rst")
if os.access(fname,os.F_OK):
    os.remove(fname)

location = "pySPACE.missions.nodes"
offset = len(location)+1
f=open(fname,"a")

######################### header ###############################################

f.write(".. AUTO-GENERATED FILE -- DO NOT EDIT! (conf.py)\n")
f.write(".. _external_nodes: \n")
f.write("\n")
f.write("Documentation of External and Wrapped Nodes \n")
f.write("=========================================== \n")
f.write("\n")
f.write("pySPACE comes along with wrappers to external algorithms.\n")

f.write("\n")
f.write("For details on the usage of the nodes and for getting usage examples, \n"
        "have a look at their documentation.\n")

node_list = []
for key, value in pySPACE.missions.nodes.DEFAULT_NODE_MAPPING.items():
    if value.__module__ == "pySPACE.missions.nodes.external":
        node_list.append(value.__module__+"."+value.__name__)
node_list.sort()

if len(node_list) > 0:
    f.write("\n")
    f.write(".. _external_folder: \n")
    f.write("\n")
    f.write("External Nodes \n")
    f.write("-------------- \n")
    f.write("\n")
    f.write("Nodes from :mod:`external folder <pySPACE.missions.nodes.external>`\n\n")
    cl = ""
    for node in node_list:
        cl += "\n:class:`" + node + "`\n"
        cl += "~"*(len(node)+9)+"\n\n"
        cl += ".. autoclass:: %s\n" % node
        cl += "    :noindex:\n\n"


    f.write(cl)
else:
    f.write("Module for external node wrapping: :mod:`pySPACE.missions.nodes.external`\n")

######################### scikit nodes #########################################

node_list = []
for key, value in pySPACE.missions.nodes.DEFAULT_NODE_MAPPING.items():
    if value.__name__.endswith("SklearnNode"):
        node_list.append(value.__module__+"."+value.__name__)
node_list.sort()

if len(node_list) > 0:
    f.write("\n")
    f.write(".. _scikit_nodes: \n")
    f.write("\n")
    f.write("Scikit Nodes \n")
    f.write("------------ \n")
    f.write("\n")
    f.write("Nodes from :mod:`scikits wrapper <pySPACE.missions.nodes.scikits_nodes>`\n\n")
    cl = ""
    for node in node_list:
        cl += "\n:class:`" + node + "`\n"
        cl += "~"*(len(node)+9)+"\n\n"
        cl += ".. autoclass:: %s\n    :no-members:\n\n" % node

    f.write(cl)

f.close()



inheritance_graph_attrs = dict(rankdir="TB",fontsize=5,ratio='compress',nodesep=0.1,sep=0.1, pad=0.001,size= '"10.0, 25.0"') #, size='""'
graphviz_output_format  = 'png' #'svg' svg is good for scaling but linking seems to work only with png
#inheritance_node_attrs = dict(shape='rectangle', fontsize=8, height=0.7,
#                              color='grey', style='filled')
inheritance_node_attrs = dict(shape='rectangle', fontsize=10, height=0.02,width=0.02,margin=0.005)
