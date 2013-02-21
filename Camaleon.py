# coding=utf8
import sublime, sublime_plugin

class CamaleonCommand(sublime_plugin.WindowCommand):
	def run(self):
		s = sublime.load_settings('Camaleon.sublime-settings')
		current = int(s.get('current'))

		next = current + 1
		if next >= len(s.get('camaleon')): # Wrap around
			next = 0
		
		for config_key in s.get('camaleon')[next].keys():
			sublime_s = sublime.load_settings('Preferences.sublime-settings')
			sublime_s.set(config_key, s.get('camaleon')[next].get(config_key));
			sublime.save_settings('Preferences.sublime-settings')

		s.set('current', next);
		sublime.save_settings('Camaleon.sublime-settings')
