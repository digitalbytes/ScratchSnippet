import sublime, sublime_plugin
import io
		
class ScratchSnippetCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		template = u"""<snippet>
	<content><![CDATA[%s]]></content>
	<tabTrigger>scratch</tabTrigger>
	<scope>%s</scope>
</snippet>
		""" % ( self.view.substr(self.view.sel()[0]), self.view.syntax_name(self.view.sel()[0].b) )

		scratch_snippet_file = os.path.join(sublime.packages_path(), 'User', 'scratch.sublime-snippet')
		with io.open(scratch_snippet_file, 'w') as file:
		    file.write(template)

	def is_enabled(self):
		return len(self.view.sel()) == 1

