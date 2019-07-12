Name:       xorg-server
Version:    1.20.3
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
%configure --enable-glamor          \
           --enable-install-setuid  \
           --enable-suid-wrapper    \
           --disable-systemd-logind \
           --with-xkb-output=/var/lib/xkb
%make_build

%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*
mkdir -pv /etc/X11/xorg.conf.d &&
mkdir -pv %{buildroot}/etc/sysconfig
cat >> %{buildroot}/etc/sysconfig/createfiles << "EOF"
/tmp/.ICE-unix dir 1777 root root
/tmp/.X11-unix dir 1777 root root
EOF

%files
/etc/sysconfig/createfiles
/usr/bin/X
/usr/bin/Xnest
/usr/bin/Xorg
/usr/bin/Xvfb
/usr/bin/cvt
/usr/bin/gtf
/usr/include/xorg/BT.h
/usr/include/xorg/IBM.h
/usr/include/xorg/TI.h
/usr/include/xorg/XIstubs.h
/usr/include/xorg/Xprintf.h
/usr/include/xorg/callback.h
/usr/include/xorg/client.h
/usr/include/xorg/closestr.h
/usr/include/xorg/closure.h
/usr/include/xorg/colormap.h
/usr/include/xorg/colormapst.h
/usr/include/xorg/compiler.h
/usr/include/xorg/compositeext.h
/usr/include/xorg/cursor.h
/usr/include/xorg/cursorstr.h
/usr/include/xorg/damage.h
/usr/include/xorg/damagestr.h
/usr/include/xorg/dbestruct.h
/usr/include/xorg/dgaproc.h
/usr/include/xorg/displaymode.h
/usr/include/xorg/dix.h
/usr/include/xorg/dixaccess.h
/usr/include/xorg/dixevents.h
/usr/include/xorg/dixfont.h
/usr/include/xorg/dixfontstr.h
/usr/include/xorg/dixgrabs.h
/usr/include/xorg/dixstruct.h
/usr/include/xorg/dri.h
/usr/include/xorg/dri2.h
/usr/include/xorg/dri3.h
/usr/include/xorg/dristruct.h
/usr/include/xorg/edid.h
/usr/include/xorg/events.h
/usr/include/xorg/exa.h
/usr/include/xorg/exevents.h
/usr/include/xorg/extension.h
/usr/include/xorg/extinit.h
/usr/include/xorg/extnsionst.h
/usr/include/xorg/fb.h
/usr/include/xorg/fbdevhw.h
/usr/include/xorg/fboverlay.h
/usr/include/xorg/fbpict.h
/usr/include/xorg/fbrop.h
/usr/include/xorg/fourcc.h
/usr/include/xorg/gc.h
/usr/include/xorg/gcstruct.h
/usr/include/xorg/geext.h
/usr/include/xorg/geint.h
/usr/include/xorg/glamor.h
/usr/include/xorg/globals.h
/usr/include/xorg/glx_extinit.h
/usr/include/xorg/glxvndabi.h
/usr/include/xorg/glyphstr.h
/usr/include/xorg/hotplug.h
/usr/include/xorg/i2c_def.h
/usr/include/xorg/input.h
/usr/include/xorg/inputstr.h
/usr/include/xorg/list.h
/usr/include/xorg/mi.h
/usr/include/xorg/micmap.h
/usr/include/xorg/micoord.h
/usr/include/xorg/migc.h
/usr/include/xorg/miline.h
/usr/include/xorg/mioverlay.h
/usr/include/xorg/mipict.h
/usr/include/xorg/mipointer.h
/usr/include/xorg/mipointrst.h
/usr/include/xorg/misc.h
/usr/include/xorg/miscstruct.h
/usr/include/xorg/mistruct.h
/usr/include/xorg/misync.h
/usr/include/xorg/misyncfd.h
/usr/include/xorg/misyncshm.h
/usr/include/xorg/misyncstr.h
/usr/include/xorg/mizerarc.h
/usr/include/xorg/nonsdk_extinit.h
/usr/include/xorg/opaque.h
/usr/include/xorg/optionstr.h
/usr/include/xorg/os.h
/usr/include/xorg/panoramiX.h
/usr/include/xorg/panoramiXsrv.h
/usr/include/xorg/picture.h
/usr/include/xorg/picturestr.h
/usr/include/xorg/pixmap.h
/usr/include/xorg/pixmapstr.h
/usr/include/xorg/present.h
/usr/include/xorg/presentext.h
/usr/include/xorg/privates.h
/usr/include/xorg/property.h
/usr/include/xorg/propertyst.h
/usr/include/xorg/ptrveloc.h
/usr/include/xorg/randrstr.h
/usr/include/xorg/region.h
/usr/include/xorg/regionstr.h
/usr/include/xorg/registry.h
/usr/include/xorg/resource.h
/usr/include/xorg/rgb.h
/usr/include/xorg/rrtransform.h
/usr/include/xorg/sarea.h
/usr/include/xorg/screenint.h
/usr/include/xorg/scrnintstr.h
/usr/include/xorg/selection.h
/usr/include/xorg/servermd.h
/usr/include/xorg/shadow.h
/usr/include/xorg/shadowfb.h
/usr/include/xorg/shmint.h
/usr/include/xorg/site.h
/usr/include/xorg/syncsdk.h
/usr/include/xorg/validate.h
/usr/include/xorg/vbe.h
/usr/include/xorg/vbeModes.h
/usr/include/xorg/vgaHW.h
/usr/include/xorg/vndserver.h
/usr/include/xorg/wfbrename.h
/usr/include/xorg/window.h
/usr/include/xorg/windowstr.h
/usr/include/xorg/xaarop.h
/usr/include/xorg/xace.h
/usr/include/xorg/xacestr.h
/usr/include/xorg/xf86.h
/usr/include/xorg/xf86Crtc.h
/usr/include/xorg/xf86Cursor.h
/usr/include/xorg/xf86DDC.h
/usr/include/xorg/xf86MatchDrivers.h
/usr/include/xorg/xf86Modes.h
/usr/include/xorg/xf86Module.h
/usr/include/xorg/xf86Opt.h
/usr/include/xorg/xf86Optionstr.h
/usr/include/xorg/xf86Optrec.h
/usr/include/xorg/xf86Parser.h
/usr/include/xorg/xf86Pci.h
/usr/include/xorg/xf86PciInfo.h
/usr/include/xorg/xf86Priv.h
/usr/include/xorg/xf86Privstr.h
/usr/include/xorg/xf86RamDac.h
/usr/include/xorg/xf86RandR12.h
/usr/include/xorg/xf86VGAarbiter.h
/usr/include/xorg/xf86Xinput.h
/usr/include/xorg/xf86_OSlib.h
/usr/include/xorg/xf86_OSproc.h
/usr/include/xorg/xf86cmap.h
/usr/include/xorg/xf86fbman.h
/usr/include/xorg/xf86i2c.h
/usr/include/xorg/xf86int10.h
/usr/include/xorg/xf86platformBus.h
/usr/include/xorg/xf86sbusBus.h
/usr/include/xorg/xf86str.h
/usr/include/xorg/xf86xv.h
/usr/include/xorg/xf86xvmc.h
/usr/include/xorg/xf86xvpriv.h
/usr/include/xorg/xisb.h
/usr/include/xorg/xkbfile.h
/usr/include/xorg/xkbrules.h
/usr/include/xorg/xkbsrv.h
/usr/include/xorg/xkbstr.h
/usr/include/xorg/xorg-server.h
/usr/include/xorg/xorgVersion.h
/usr/include/xorg/xserver-properties.h
/usr/include/xorg/xserver_poll.h
/usr/include/xorg/xvdix.h
/usr/include/xorg/xvmcext.h
/usr/lib64/pkgconfig/xorg-server.pc
/usr/lib64/xorg/modules/drivers/modesetting_drv.la
/usr/lib64/xorg/modules/drivers/modesetting_drv.so
/usr/lib64/xorg/modules/extensions/libglx.la
/usr/lib64/xorg/modules/extensions/libglx.so
/usr/lib64/xorg/modules/libexa.la
/usr/lib64/xorg/modules/libexa.so
/usr/lib64/xorg/modules/libfb.la
/usr/lib64/xorg/modules/libfb.so
/usr/lib64/xorg/modules/libfbdevhw.la
/usr/lib64/xorg/modules/libfbdevhw.so
/usr/lib64/xorg/modules/libglamoregl.la
/usr/lib64/xorg/modules/libglamoregl.so
/usr/lib64/xorg/modules/libint10.la
/usr/lib64/xorg/modules/libint10.so
/usr/lib64/xorg/modules/libshadow.la
/usr/lib64/xorg/modules/libshadow.so
/usr/lib64/xorg/modules/libshadowfb.la
/usr/lib64/xorg/modules/libshadowfb.so
/usr/lib64/xorg/modules/libvbe.la
/usr/lib64/xorg/modules/libvbe.so
/usr/lib64/xorg/modules/libvgahw.la
/usr/lib64/xorg/modules/libvgahw.so
/usr/lib64/xorg/modules/libwfb.la
/usr/lib64/xorg/modules/libwfb.so
/usr/lib64/xorg/protocol.txt
/usr/libexec/Xorg
/usr/libexec/Xorg.wrap
/usr/share/X11/xorg.conf.d/10-quirks.conf
/usr/share/aclocal/xorg-server.m4
/usr/share/man/man1/Xnest.1.gz
/usr/share/man/man1/Xorg.1.gz
/usr/share/man/man1/Xorg.wrap.1.gz
/usr/share/man/man1/Xserver.1.gz
/usr/share/man/man1/Xvfb.1.gz
/usr/share/man/man1/cvt.1.gz
/usr/share/man/man1/gtf.1.gz
/usr/share/man/man4/exa.4.gz
/usr/share/man/man4/fbdevhw.4.gz
/usr/share/man/man4/modesetting.4.gz
/usr/share/man/man5/Xwrapper.config.5.gz
/usr/share/man/man5/xorg.conf.5.gz
/usr/share/man/man5/xorg.conf.d.5.gz
/var/lib/xkb/README.compiled

%changelog
# let's skip this for now

