import sublime
import sublime_plugin


class HotProjectExit(sublime_plugin.WindowCommand):
    def run(self):
        for v in self.window.views():
            if v.is_dirty():
                v.run_command("save")
        self.window.run_command("close_workspace")
        self.window.run_command('set_layout', {
            "cols": [0.0, 1.0],
            "rows": [0.0, 1.0],
            "cells": [[0, 0, 1, 1]]
        })
        self.window.run_command("close_window")
