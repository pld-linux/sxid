Summary:	suid, sgid file and directory checking
Summary(pl):	sprawdza pliki i katalogi o atrybutach suid i sgid
Name:		sxid
Version:	4.0.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://marcus.seva.net/pub/sxid/%{name}_%{version}.tar.gz
BuildRequires:	autoconf
Requires:	crondaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/%{name}

%description
This program runs as a cronjob. Basically it tracks any changes in
your s[ug]id files and folders. If there are any new ones, ones that
aren't set any more, or they have changed bits or other modes then it
reports the changes. You can also run this manually for spot checking.

It tracks s[ug]id files by md5 checksums. This helps detect if your
files have been tampered with, would not show under normal name and
permissions checking. Directories are tracked by inodes.

%description -l pl
Ten program jest uruchamiany z crondaemon'a. ¦ledzi on zmiany w
plikach i katalogach o atrybutach s[ug]id. Je¿eli pojawiaj± sie nowe,
takie których jeszcze nie zna lub takie, które sie zmieni³y wtedy
raportuje zmiany. Mo¿na go tak¿e uruchamiaæ rêcznie do
natychmiastowych sprawdzeñ.

%prep
%setup -q

%build
autoconf
%configure
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT/etc/cron.daily
install debian/cron.daily $RPM_BUILD_ROOT/etc/cron.daily/sxid

gzip -9nf README docs/sxid.conf.example

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz docs/sxid.conf.example.gz
%attr(755,root,root) %{_bindir}/*
%attr(700,root,root) /etc/cron.daily/sxid
%{_mandir}/*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
