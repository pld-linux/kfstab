Summary:	A program for easy modifying file /etc/fstab
Summary(pl):	Program do ³atwej modyfikacji pliku /etc/fstab
Name:		kfstab
Version:	0.7.0
Release:	2
License:	GPL v2
Vendor:		Andreas Reuter <Andreas.Reuter@andreas-reuter.de>
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kfstab/%{name}-%{version}.tgz
# Source0-md5:	558ecd04b0924df30fd822192422e030
Patch0:		%{name}-morefilesystems.patch
Patch1:		%{name}-desktopfile.patch
URL:		http://kfstab.sourceforge.net/
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.0.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdelibs >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A program for easy modifying /etc/fstab .

%description -l pl
Program do ³atwej modyfikacji pliku /etc/fstab .

%prep
%setup -q -n %{name} 
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* admin
%configure \
	KDEDIR=%{_libdir} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/System/%{name}.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_desktopdir}/*
%{_iconsdir}/*/*/*/*
