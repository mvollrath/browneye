Name:       sqlite3
Version:    324
Release:    1
Summary:    SQLlite database engine.
License:    GPL
Source0:    sqlite-autoconf-3240000.tar.gz
Prefix:     /usr

%description


%prep
%setup -n sqlite-autoconf-3240000

%build
%configure --disable-static  \
            --enable-fts5     \
            CFLAGS="-g -O2                    \
            -DSQLITE_ENABLE_FTS4=1            \
            -DSQLITE_ENABLE_COLUMN_METADATA=1 \
            -DSQLITE_ENABLE_UNLOCK_NOTIFY=1   \
            -DSQLITE_ENABLE_DBSTAT_VTAB=1     \
            -DSQLITE_SECURE_DELETE=1          \
            -DSQLITE_ENABLE_FTS3_TOKENIZER=1"
%make_build

%install
rm -rf %{buildroot}
%make_install

%files
/usr/bin/sqlite3
/usr/include/sqlite3.h
/usr/include/sqlite3ext.h
/usr/lib64/libsqlite3.la
/usr/lib64/libsqlite3.so
/usr/lib64/libsqlite3.so.0
/usr/lib64/libsqlite3.so.0.8.6
/usr/lib64/pkgconfig/sqlite3.pc
/usr/share/man/man1/sqlite3.1.gz

%changelog
* Tue Dec 10 2019 Chris Statzer <chris.statzer@qq.com> 324
- Initial RPM

