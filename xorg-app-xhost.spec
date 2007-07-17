Summary:	xhost - server access control program for X
Summary(pl.UTF-8):	xhost - program do kontroli dostępu do serwera X
Name:		xorg-app-xhost
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xhost-%{version}.tar.bz2
# Source0-md5:	f746aba36f075ae4cae313d849a94f4e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXau-devel
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xhost program is used to add and delete host names or user names
to the list allowed to make connections to the X server.

%description -l pl.UTF-8
Program xhost służy do dodawania i usuwania nazw hostów lub
użytkowników do/z listy zezwalającej na wykonywanie połączeń do
serwera X.

%prep
%setup -q -n xhost-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xhost
%{_mandir}/man1/xhost.1x*
