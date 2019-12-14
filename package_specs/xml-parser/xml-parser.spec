Name:       XML-Parser
Version:    2.44
Release:    1
Summary:    TODO
License:    GPL3
Source0:    %{name}-%{version}.tar.gz
Prefix:     /usr

%description
TODO

%prep
%setup -q -a0

%build
perl Makefile.PL
%make_build

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT
rm -vf %{buildroot}%{_infodir}/dir*
rm -f %{buildroot}/usr/lib/perl5/5.28.1/x86_64-linux-thread-multi/perllocal.pod

%files
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/Japanese_Encodings.msg
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/README
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/big5.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/euc-kr.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/ibm866.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-2.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-3.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-4.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-5.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-7.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-8.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/iso-8859-9.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/koi8-r.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/windows-1250.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/windows-1251.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/windows-1252.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/windows-1255.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-euc-jp-jisx0221.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-euc-jp-unicode.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-sjis-cp932.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-sjis-jdk117.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-sjis-jisx0221.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Encodings/x-sjis-unicode.enc
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Expat.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/LWPExternEnt.pl
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Style/Debug.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Style/Objects.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Style/Stream.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Style/Subs.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/XML/Parser/Style/Tree.pm
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/XML/Parser/.packlist
/usr/lib/perl5/site_perl/5.28.1/x86_64-linux-thread-multi/auto/XML/Parser/Expat/Expat.so
/usr/share/man/man3/XML::Parser.3.gz
/usr/share/man/man3/XML::Parser::Expat.3.gz
/usr/share/man/man3/XML::Parser::Style::Debug.3.gz
/usr/share/man/man3/XML::Parser::Style::Objects.3.gz
/usr/share/man/man3/XML::Parser::Style::Stream.3.gz
/usr/share/man/man3/XML::Parser::Style::Subs.3.gz
/usr/share/man/man3/XML::Parser::Style::Tree.3.gz

%changelog
# let's skip this for now
