Name:       awesome
Version:    4.3
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}.tar.bz2

%description
TODO

%prep
%setup -a 0

%build
mkdir build
pushd build
cmake .. -DPREFIX=/usr
make
popd


%install    
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/local/bin/awesome
/usr/local/bin/awesome-client
/usr/local/etc/xdg/awesome/rc.lua
/usr/local/share/awesome/icons/awesome16.png
/usr/local/share/awesome/icons/awesome32.png
/usr/local/share/awesome/icons/awesome48.png
/usr/local/share/awesome/icons/awesome64.png
/usr/local/share/awesome/lib/awful/autofocus.lua
/usr/local/share/awesome/lib/awful/button.lua
/usr/local/share/awesome/lib/awful/client.lua
/usr/local/share/awesome/lib/awful/client/focus.lua
/usr/local/share/awesome/lib/awful/client/shape.lua
/usr/local/share/awesome/lib/awful/client/urgent.lua
/usr/local/share/awesome/lib/awful/completion.lua
/usr/local/share/awesome/lib/awful/dbus.lua
/usr/local/share/awesome/lib/awful/ewmh.lua
/usr/local/share/awesome/lib/awful/hotkeys_popup/init.lua
/usr/local/share/awesome/lib/awful/hotkeys_popup/keys/firefox.lua
/usr/local/share/awesome/lib/awful/hotkeys_popup/keys/init.lua
/usr/local/share/awesome/lib/awful/hotkeys_popup/keys/qutebrowser.lua
/usr/local/share/awesome/lib/awful/hotkeys_popup/keys/termite.lua
/usr/local/share/awesome/lib/awful/hotkeys_popup/keys/tmux.lua
/usr/local/share/awesome/lib/awful/hotkeys_popup/keys/vim.lua
/usr/local/share/awesome/lib/awful/hotkeys_popup/widget.lua
/usr/local/share/awesome/lib/awful/init.lua
/usr/local/share/awesome/lib/awful/key.lua
/usr/local/share/awesome/lib/awful/keygrabber.lua
/usr/local/share/awesome/lib/awful/layout/init.lua
/usr/local/share/awesome/lib/awful/layout/suit/corner.lua
/usr/local/share/awesome/lib/awful/layout/suit/fair.lua
/usr/local/share/awesome/lib/awful/layout/suit/floating.lua
/usr/local/share/awesome/lib/awful/layout/suit/init.lua
/usr/local/share/awesome/lib/awful/layout/suit/magnifier.lua
/usr/local/share/awesome/lib/awful/layout/suit/max.lua
/usr/local/share/awesome/lib/awful/layout/suit/spiral.lua
/usr/local/share/awesome/lib/awful/layout/suit/tile.lua
/usr/local/share/awesome/lib/awful/menu.lua
/usr/local/share/awesome/lib/awful/mouse/drag_to_tag.lua
/usr/local/share/awesome/lib/awful/mouse/init.lua
/usr/local/share/awesome/lib/awful/mouse/resize.lua
/usr/local/share/awesome/lib/awful/mouse/snap.lua
/usr/local/share/awesome/lib/awful/placement.lua
/usr/local/share/awesome/lib/awful/popup.lua
/usr/local/share/awesome/lib/awful/prompt.lua
/usr/local/share/awesome/lib/awful/remote.lua
/usr/local/share/awesome/lib/awful/rules.lua
/usr/local/share/awesome/lib/awful/screen.lua
/usr/local/share/awesome/lib/awful/spawn.lua
/usr/local/share/awesome/lib/awful/startup_notification.lua
/usr/local/share/awesome/lib/awful/tag.lua
/usr/local/share/awesome/lib/awful/titlebar.lua
/usr/local/share/awesome/lib/awful/tooltip.lua
/usr/local/share/awesome/lib/awful/util.lua
/usr/local/share/awesome/lib/awful/wibar.lua
/usr/local/share/awesome/lib/awful/wibox.lua
/usr/local/share/awesome/lib/awful/widget/button.lua
/usr/local/share/awesome/lib/awful/widget/calendar_popup.lua
/usr/local/share/awesome/lib/awful/widget/clienticon.lua
/usr/local/share/awesome/lib/awful/widget/common.lua
/usr/local/share/awesome/lib/awful/widget/graph.lua
/usr/local/share/awesome/lib/awful/widget/init.lua
/usr/local/share/awesome/lib/awful/widget/keyboardlayout.lua
/usr/local/share/awesome/lib/awful/widget/launcher.lua
/usr/local/share/awesome/lib/awful/widget/layoutbox.lua
/usr/local/share/awesome/lib/awful/widget/layoutlist.lua
/usr/local/share/awesome/lib/awful/widget/only_on_screen.lua
/usr/local/share/awesome/lib/awful/widget/progressbar.lua
/usr/local/share/awesome/lib/awful/widget/prompt.lua
/usr/local/share/awesome/lib/awful/widget/taglist.lua
/usr/local/share/awesome/lib/awful/widget/tasklist.lua
/usr/local/share/awesome/lib/awful/widget/textclock.lua
/usr/local/share/awesome/lib/awful/widget/watch.lua
/usr/local/share/awesome/lib/beautiful.lua
/usr/local/share/awesome/lib/beautiful/gtk.lua
/usr/local/share/awesome/lib/beautiful/init.lua
/usr/local/share/awesome/lib/beautiful/theme_assets.lua
/usr/local/share/awesome/lib/beautiful/xresources.lua
/usr/local/share/awesome/lib/gears/cache.lua
/usr/local/share/awesome/lib/gears/color.lua
/usr/local/share/awesome/lib/gears/debug.lua
/usr/local/share/awesome/lib/gears/filesystem.lua
/usr/local/share/awesome/lib/gears/geometry.lua
/usr/local/share/awesome/lib/gears/init.lua
/usr/local/share/awesome/lib/gears/math.lua
/usr/local/share/awesome/lib/gears/matrix.lua
/usr/local/share/awesome/lib/gears/object.lua
/usr/local/share/awesome/lib/gears/object/properties.lua
/usr/local/share/awesome/lib/gears/protected_call.lua
/usr/local/share/awesome/lib/gears/shape.lua
/usr/local/share/awesome/lib/gears/sort/init.lua
/usr/local/share/awesome/lib/gears/sort/topological.lua
/usr/local/share/awesome/lib/gears/string.lua
/usr/local/share/awesome/lib/gears/surface.lua
/usr/local/share/awesome/lib/gears/table.lua
/usr/local/share/awesome/lib/gears/timer.lua
/usr/local/share/awesome/lib/gears/wallpaper.lua
/usr/local/share/awesome/lib/menubar/icon_theme.lua
/usr/local/share/awesome/lib/menubar/index_theme.lua
/usr/local/share/awesome/lib/menubar/init.lua
/usr/local/share/awesome/lib/menubar/menu_gen.lua
/usr/local/share/awesome/lib/menubar/utils.lua
/usr/local/share/awesome/lib/naughty.lua
/usr/local/share/awesome/lib/naughty/core.lua
/usr/local/share/awesome/lib/naughty/dbus.lua
/usr/local/share/awesome/lib/naughty/init.lua
/usr/local/share/awesome/lib/wibox/container/arcchart.lua
/usr/local/share/awesome/lib/wibox/container/background.lua
/usr/local/share/awesome/lib/wibox/container/constraint.lua
/usr/local/share/awesome/lib/wibox/container/init.lua
/usr/local/share/awesome/lib/wibox/container/margin.lua
/usr/local/share/awesome/lib/wibox/container/mirror.lua
/usr/local/share/awesome/lib/wibox/container/place.lua
/usr/local/share/awesome/lib/wibox/container/radialprogressbar.lua
/usr/local/share/awesome/lib/wibox/container/rotate.lua
/usr/local/share/awesome/lib/wibox/container/scroll.lua
/usr/local/share/awesome/lib/wibox/drawable.lua
/usr/local/share/awesome/lib/wibox/hierarchy.lua
/usr/local/share/awesome/lib/wibox/init.lua
/usr/local/share/awesome/lib/wibox/layout/align.lua
/usr/local/share/awesome/lib/wibox/layout/constraint.lua
/usr/local/share/awesome/lib/wibox/layout/fixed.lua
/usr/local/share/awesome/lib/wibox/layout/flex.lua
/usr/local/share/awesome/lib/wibox/layout/grid.lua
/usr/local/share/awesome/lib/wibox/layout/init.lua
/usr/local/share/awesome/lib/wibox/layout/manual.lua
/usr/local/share/awesome/lib/wibox/layout/margin.lua
/usr/local/share/awesome/lib/wibox/layout/mirror.lua
/usr/local/share/awesome/lib/wibox/layout/ratio.lua
/usr/local/share/awesome/lib/wibox/layout/rotate.lua
/usr/local/share/awesome/lib/wibox/layout/scroll.lua
/usr/local/share/awesome/lib/wibox/layout/stack.lua
/usr/local/share/awesome/lib/wibox/widget/background.lua
/usr/local/share/awesome/lib/wibox/widget/base.lua
/usr/local/share/awesome/lib/wibox/widget/calendar.lua
/usr/local/share/awesome/lib/wibox/widget/checkbox.lua
/usr/local/share/awesome/lib/wibox/widget/graph.lua
/usr/local/share/awesome/lib/wibox/widget/imagebox.lua
/usr/local/share/awesome/lib/wibox/widget/init.lua
/usr/local/share/awesome/lib/wibox/widget/piechart.lua
/usr/local/share/awesome/lib/wibox/widget/progressbar.lua
/usr/local/share/awesome/lib/wibox/widget/separator.lua
/usr/local/share/awesome/lib/wibox/widget/slider.lua
/usr/local/share/awesome/lib/wibox/widget/systray.lua
/usr/local/share/awesome/lib/wibox/widget/textbox.lua
/usr/local/share/awesome/lib/wibox/widget/textclock.lua
/usr/local/share/awesome/themes/default/README
/usr/local/share/awesome/themes/default/background.png
/usr/local/share/awesome/themes/default/background_white.png
/usr/local/share/awesome/themes/default/layouts/cornerne.png
/usr/local/share/awesome/themes/default/layouts/cornernew.png
/usr/local/share/awesome/themes/default/layouts/cornernw.png
/usr/local/share/awesome/themes/default/layouts/cornernww.png
/usr/local/share/awesome/themes/default/layouts/cornerse.png
/usr/local/share/awesome/themes/default/layouts/cornersew.png
/usr/local/share/awesome/themes/default/layouts/cornersw.png
/usr/local/share/awesome/themes/default/layouts/cornersww.png
/usr/local/share/awesome/themes/default/layouts/dwindle.png
/usr/local/share/awesome/themes/default/layouts/dwindlew.png
/usr/local/share/awesome/themes/default/layouts/fairh.png
/usr/local/share/awesome/themes/default/layouts/fairhw.png
/usr/local/share/awesome/themes/default/layouts/fairv.png
/usr/local/share/awesome/themes/default/layouts/fairvw.png
/usr/local/share/awesome/themes/default/layouts/floating.png
/usr/local/share/awesome/themes/default/layouts/floatingw.png
/usr/local/share/awesome/themes/default/layouts/fullscreen.png
/usr/local/share/awesome/themes/default/layouts/fullscreenw.png
/usr/local/share/awesome/themes/default/layouts/magnifier.png
/usr/local/share/awesome/themes/default/layouts/magnifierw.png
/usr/local/share/awesome/themes/default/layouts/max.png
/usr/local/share/awesome/themes/default/layouts/maxw.png
/usr/local/share/awesome/themes/default/layouts/spiral.png
/usr/local/share/awesome/themes/default/layouts/spiralw.png
/usr/local/share/awesome/themes/default/layouts/tile.png
/usr/local/share/awesome/themes/default/layouts/tilebottom.png
/usr/local/share/awesome/themes/default/layouts/tilebottomw.png
/usr/local/share/awesome/themes/default/layouts/tileleft.png
/usr/local/share/awesome/themes/default/layouts/tileleftw.png
/usr/local/share/awesome/themes/default/layouts/tiletop.png
/usr/local/share/awesome/themes/default/layouts/tiletopw.png
/usr/local/share/awesome/themes/default/layouts/tilew.png
/usr/local/share/awesome/themes/default/submenu.png
/usr/local/share/awesome/themes/default/taglist/squarefw.png
/usr/local/share/awesome/themes/default/taglist/squarew.png
/usr/local/share/awesome/themes/default/theme.lua
/usr/local/share/awesome/themes/default/titlebar/close_focus.png
/usr/local/share/awesome/themes/default/titlebar/close_normal.png
/usr/local/share/awesome/themes/default/titlebar/floating_focus_active.png
/usr/local/share/awesome/themes/default/titlebar/floating_focus_inactive.png
/usr/local/share/awesome/themes/default/titlebar/floating_normal_active.png
/usr/local/share/awesome/themes/default/titlebar/floating_normal_inactive.png
/usr/local/share/awesome/themes/default/titlebar/maximized_focus_active.png
/usr/local/share/awesome/themes/default/titlebar/maximized_focus_inactive.png
/usr/local/share/awesome/themes/default/titlebar/maximized_normal_active.png
/usr/local/share/awesome/themes/default/titlebar/maximized_normal_inactive.png
/usr/local/share/awesome/themes/default/titlebar/minimize_focus.png
/usr/local/share/awesome/themes/default/titlebar/minimize_normal.png
/usr/local/share/awesome/themes/default/titlebar/ontop_focus_active.png
/usr/local/share/awesome/themes/default/titlebar/ontop_focus_inactive.png
/usr/local/share/awesome/themes/default/titlebar/ontop_normal_active.png
/usr/local/share/awesome/themes/default/titlebar/ontop_normal_inactive.png
/usr/local/share/awesome/themes/default/titlebar/sticky_focus_active.png
/usr/local/share/awesome/themes/default/titlebar/sticky_focus_inactive.png
/usr/local/share/awesome/themes/default/titlebar/sticky_normal_active.png
/usr/local/share/awesome/themes/default/titlebar/sticky_normal_inactive.png
/usr/local/share/awesome/themes/gtk/theme.lua
/usr/local/share/awesome/themes/sky/awesome-icon.png
/usr/local/share/awesome/themes/sky/layouts/cornerne.png
/usr/local/share/awesome/themes/sky/layouts/cornernw.png
/usr/local/share/awesome/themes/sky/layouts/cornerse.png
/usr/local/share/awesome/themes/sky/layouts/cornersw.png
/usr/local/share/awesome/themes/sky/layouts/dwindle.png
/usr/local/share/awesome/themes/sky/layouts/fairh.png
/usr/local/share/awesome/themes/sky/layouts/fairv.png
/usr/local/share/awesome/themes/sky/layouts/floating.png
/usr/local/share/awesome/themes/sky/layouts/fullscreen.png
/usr/local/share/awesome/themes/sky/layouts/magnifier.png
/usr/local/share/awesome/themes/sky/layouts/max.png
/usr/local/share/awesome/themes/sky/layouts/spiral.png
/usr/local/share/awesome/themes/sky/layouts/tile.png
/usr/local/share/awesome/themes/sky/layouts/tilebottom.png
/usr/local/share/awesome/themes/sky/layouts/tileleft.png
/usr/local/share/awesome/themes/sky/layouts/tiletop.png
/usr/local/share/awesome/themes/sky/sky-background.png
/usr/local/share/awesome/themes/sky/theme.lua
/usr/local/share/awesome/themes/xresources/assets.lua
/usr/local/share/awesome/themes/xresources/theme.lua
/usr/local/share/awesome/themes/zenburn/awesome-icon.png
/usr/local/share/awesome/themes/zenburn/layouts/cornerne.png
/usr/local/share/awesome/themes/zenburn/layouts/cornernw.png
/usr/local/share/awesome/themes/zenburn/layouts/cornerse.png
/usr/local/share/awesome/themes/zenburn/layouts/cornersw.png
/usr/local/share/awesome/themes/zenburn/layouts/dwindle.png
/usr/local/share/awesome/themes/zenburn/layouts/fairh.png
/usr/local/share/awesome/themes/zenburn/layouts/fairv.png
/usr/local/share/awesome/themes/zenburn/layouts/floating.png
/usr/local/share/awesome/themes/zenburn/layouts/fullscreen.png
/usr/local/share/awesome/themes/zenburn/layouts/magnifier.png
/usr/local/share/awesome/themes/zenburn/layouts/max.png
/usr/local/share/awesome/themes/zenburn/layouts/spiral.png
/usr/local/share/awesome/themes/zenburn/layouts/tile.png
/usr/local/share/awesome/themes/zenburn/layouts/tilebottom.png
/usr/local/share/awesome/themes/zenburn/layouts/tileleft.png
/usr/local/share/awesome/themes/zenburn/layouts/tiletop.png
/usr/local/share/awesome/themes/zenburn/taglist/squarefz.png
/usr/local/share/awesome/themes/zenburn/taglist/squarez.png
/usr/local/share/awesome/themes/zenburn/theme.lua
/usr/local/share/awesome/themes/zenburn/titlebar/close_focus.png
/usr/local/share/awesome/themes/zenburn/titlebar/close_normal.png
/usr/local/share/awesome/themes/zenburn/titlebar/floating_focus_active.png
/usr/local/share/awesome/themes/zenburn/titlebar/floating_focus_inactive.png
/usr/local/share/awesome/themes/zenburn/titlebar/floating_normal_active.png
/usr/local/share/awesome/themes/zenburn/titlebar/floating_normal_inactive.png
/usr/local/share/awesome/themes/zenburn/titlebar/maximized_focus_active.png
/usr/local/share/awesome/themes/zenburn/titlebar/maximized_focus_inactive.png
/usr/local/share/awesome/themes/zenburn/titlebar/maximized_normal_active.png
/usr/local/share/awesome/themes/zenburn/titlebar/maximized_normal_inactive.png
/usr/local/share/awesome/themes/zenburn/titlebar/ontop_focus_active.png
/usr/local/share/awesome/themes/zenburn/titlebar/ontop_focus_inactive.png
/usr/local/share/awesome/themes/zenburn/titlebar/ontop_normal_active.png
/usr/local/share/awesome/themes/zenburn/titlebar/ontop_normal_inactive.png
/usr/local/share/awesome/themes/zenburn/titlebar/sticky_focus_active.png
/usr/local/share/awesome/themes/zenburn/titlebar/sticky_focus_inactive.png
/usr/local/share/awesome/themes/zenburn/titlebar/sticky_normal_active.png
/usr/local/share/awesome/themes/zenburn/titlebar/sticky_normal_inactive.png
/usr/local/share/awesome/themes/zenburn/zenburn-background.png
/usr/local/share/doc/awesome/00-authors.md
/usr/local/share/doc/awesome/01-readme.md
/usr/local/share/doc/awesome/02-contributing.md
/usr/local/share/doc/awesome/LICENSE
/usr/local/share/xsessions/awesome.desktop


%changelog
# let's skip this for now

