import sublime, sublime_plugin
import io
import os
import xml.dom.minidom
		
class ScratchSnippetCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		impl = xml.dom.minidom.getDOMImplementation()

		snippet_doc = impl.createDocument(None, "snippet", None)
		snippet = snippet_doc.documentElement
		content = snippet_doc.createElement('content')
		content.appendChild(snippet_doc.createCDATASection( self.view.substr(self.view.sel()[0]) ))
		snippet.appendChild(content)
		tabTrigger = snippet_doc.createElement('tabTrigger')
		tabTrigger.appendChild(snippet_doc.createTextNode('scratch'))

		scratch_snippet_path = os.path.join(sublime.packages_path(), 'User', 'scratch.sublime-snippet')
		with io.open(scratch_snippet_path, 'w') as file:
			file.write(snippet_doc.toxml())

	def is_enabled(self):
		return len(self.view.sel()) == 1

class InsertScratchSnippetCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		snippet_path = os.path.join(sublime.packages_path(), 'User', 'scratch.sublime-snippet')
		dom = xml.dom.minidom.parse(snippet_path)
		template = dom.lastChild.getElementsByTagName('content')[0].firstChild.nodeValue

		self.view.run_command( 'insert_snippet', { 'contents':template.strip() } )