Name:       slang
Version:    2.3.2
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
%configure  --prefix=/usr \
            --sysconfdir=/etc \
            --with-readline=gnu
%make_build -j1


%install    
rm -rf %{buildroot}
%make_install
rm -vf %{buildroot}%{_infodir}/dir*

%files
/etc/slsh.rc
/usr/bin/slsh
/usr/include/slang.h
/usr/include/slcurses.h
/usr/lib64/libslang.so
/usr/lib64/libslang.so.2
/usr/lib64/libslang.so.2.3.2
/usr/lib64/pkgconfig/slang.pc
/usr/lib64/slang/v2/modules/base64-module.so
/usr/lib64/slang/v2/modules/chksum-module.so
/usr/lib64/slang/v2/modules/csv-module.so
/usr/lib64/slang/v2/modules/fcntl-module.so
/usr/lib64/slang/v2/modules/fork-module.so
/usr/lib64/slang/v2/modules/histogram-module.so
/usr/lib64/slang/v2/modules/iconv-module.so
/usr/lib64/slang/v2/modules/json-module.so
/usr/lib64/slang/v2/modules/pcre-module.so
/usr/lib64/slang/v2/modules/png-module.so
/usr/lib64/slang/v2/modules/rand-module.so
/usr/lib64/slang/v2/modules/select-module.so
/usr/lib64/slang/v2/modules/slsmg-module.so
/usr/lib64/slang/v2/modules/socket-module.so
/usr/lib64/slang/v2/modules/stats-module.so
/usr/lib64/slang/v2/modules/sysconf-module.so
/usr/lib64/slang/v2/modules/termios-module.so
/usr/lib64/slang/v2/modules/varray-module.so
/usr/lib64/slang/v2/modules/zlib-module.so
/usr/share/doc/slang/v2/COPYING
/usr/share/doc/slang/v2/changes.txt
/usr/share/doc/slang/v2/cref.txt
/usr/share/doc/slang/v2/cslang.txt
/usr/share/doc/slang/v2/slang.txt
/usr/share/doc/slang/v2/slangdoc.html
/usr/share/doc/slang/v2/slangfun.txt
/usr/share/doc/slsh/html/slshfun-1.html
/usr/share/doc/slsh/html/slshfun-10.html
/usr/share/doc/slsh/html/slshfun-11.html
/usr/share/doc/slsh/html/slshfun-12.html
/usr/share/doc/slsh/html/slshfun-13.html
/usr/share/doc/slsh/html/slshfun-2.html
/usr/share/doc/slsh/html/slshfun-3.html
/usr/share/doc/slsh/html/slshfun-4.html
/usr/share/doc/slsh/html/slshfun-5.html
/usr/share/doc/slsh/html/slshfun-6.html
/usr/share/doc/slsh/html/slshfun-7.html
/usr/share/doc/slsh/html/slshfun-8.html
/usr/share/doc/slsh/html/slshfun-9.html
/usr/share/doc/slsh/html/slshfun.html
/usr/share/man/man1/slsh.1.gz
/usr/share/slsh/arrayfuns.sl
/usr/share/slsh/autoload.sl
/usr/share/slsh/base64.sl
/usr/share/slsh/chksum.sl
/usr/share/slsh/cmaps/cool.map
/usr/share/slsh/cmaps/coolwarm.map
/usr/share/slsh/cmaps/copper.map
/usr/share/slsh/cmaps/cubicl.map
/usr/share/slsh/cmaps/cubicyf.map
/usr/share/slsh/cmaps/drywet.map
/usr/share/slsh/cmaps/ds9b.map
/usr/share/slsh/cmaps/ds9sls.map
/usr/share/slsh/cmaps/edge.map
/usr/share/slsh/cmaps/gebco.map
/usr/share/slsh/cmaps/globe.map
/usr/share/slsh/cmaps/gray.map
/usr/share/slsh/cmaps/haxby.map
/usr/share/slsh/cmaps/hot.map
/usr/share/slsh/cmaps/jet.map
/usr/share/slsh/cmaps/no_green.map
/usr/share/slsh/cmaps/ocean.map
/usr/share/slsh/cmaps/polar.map
/usr/share/slsh/cmaps/rainbow.map
/usr/share/slsh/cmaps/red2green.map
/usr/share/slsh/cmaps/relief.map
/usr/share/slsh/cmaps/sealand.map
/usr/share/slsh/cmaps/seis.map
/usr/share/slsh/cmaps/split.map
/usr/share/slsh/cmaps/topo.map
/usr/share/slsh/cmaps/wysiwyg.map
/usr/share/slsh/cmdopt.sl
/usr/share/slsh/csv.sl
/usr/share/slsh/fcntl.sl
/usr/share/slsh/fork.sl
/usr/share/slsh/fswalk.sl
/usr/share/slsh/glob.sl
/usr/share/slsh/help/arrayfuns.hlp
/usr/share/slsh/help/base64funs.hlp
/usr/share/slsh/help/chksumfuns.hlp
/usr/share/slsh/help/cmdopt.hlp
/usr/share/slsh/help/csvfuns.hlp
/usr/share/slsh/help/forkfuns.hlp
/usr/share/slsh/help/fswalk.hlp
/usr/share/slsh/help/glob.hlp
/usr/share/slsh/help/histfuns.hlp
/usr/share/slsh/help/jsonfuns.hlp
/usr/share/slsh/help/listfuns.hlp
/usr/share/slsh/help/onigfuns.hlp
/usr/share/slsh/help/pcrefuns.hlp
/usr/share/slsh/help/pngfuns.hlp
/usr/share/slsh/help/print.hlp
/usr/share/slsh/help/process.hlp
/usr/share/slsh/help/profile.hlp
/usr/share/slsh/help/randfuns.hlp
/usr/share/slsh/help/readascii.hlp
/usr/share/slsh/help/require.hlp
/usr/share/slsh/help/setfuns.hlp
/usr/share/slsh/help/slsmg.hlp
/usr/share/slsh/help/sockfuns.hlp
/usr/share/slsh/help/statsfuns.hlp
/usr/share/slsh/help/structfuns.hlp
/usr/share/slsh/histogram.sl
/usr/share/slsh/iconv.sl
/usr/share/slsh/json.sl
/usr/share/slsh/listfuns.sl
/usr/share/slsh/onig.sl
/usr/share/slsh/pcre.sl
/usr/share/slsh/png.sl
/usr/share/slsh/print.sl
/usr/share/slsh/process.sl
/usr/share/slsh/profile.sl
/usr/share/slsh/rand.sl
/usr/share/slsh/readascii.sl
/usr/share/slsh/require.sl
/usr/share/slsh/rline/complete.sl
/usr/share/slsh/rline/editfuns.sl
/usr/share/slsh/rline/editor.sl
/usr/share/slsh/rline/emacskeys.sl
/usr/share/slsh/rline/history.sl
/usr/share/slsh/rline/histsrch.sl
/usr/share/slsh/rline/slrline.rc
/usr/share/slsh/rline/vikeys.sl
/usr/share/slsh/scripts/jpegsize
/usr/share/slsh/scripts/lsrpm
/usr/share/slsh/scripts/sldb
/usr/share/slsh/scripts/slprof
/usr/share/slsh/scripts/slstkchk
/usr/share/slsh/scripts/svnsh
/usr/share/slsh/select.sl
/usr/share/slsh/setfuns.sl
/usr/share/slsh/sldb.sl
/usr/share/slsh/sldbcore.sl
/usr/share/slsh/sldbsock.sl
/usr/share/slsh/slshhelp.sl
/usr/share/slsh/slshrl.sl
/usr/share/slsh/slsmg.sl
/usr/share/slsh/socket.sl
/usr/share/slsh/stats.sl
/usr/share/slsh/statslib/ad_test.sl
/usr/share/slsh/statslib/ks_test.sl
/usr/share/slsh/statslib/kuiper.sl
/usr/share/slsh/stkcheck.sl
/usr/share/slsh/structfuns.sl
/usr/share/slsh/sysconf.sl
/usr/share/slsh/termios.sl
/usr/share/slsh/varray.sl
/usr/share/slsh/zlib.sl


%changelog
# let's skip this for now

