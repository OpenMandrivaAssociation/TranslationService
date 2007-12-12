Name:               TranslationService
Summary:            A Zope product to provide translation
Version:            0.4
Release:            %mkrel 1
Group:              Development/Python
Requires:           zope
License:            GPL
URL:                http://www.zope.org/Members/efge/TranslationService
Packager:           Sebastien Robin <seb@nexedi.com>
BuildRoot:          %{_tmppath}/%{name}-%{version}-rootdir
Buildarch:          noarch

Source: %{name}-%{version}.tar.bz2

#----------------------------------------------------------------------
%description
TranslationService is a placeful translation service for Zope 2.6.

It allows you to have fully functional internationalization from Page
Templates using the standardized i18n tags.

#----------------------------------------------------------------------
%prep

rm -rf $RPM_BUILD_ROOT
%setup -a 0

#----------------------------------------------------------------------
%build

#----------------------------------------------------------------------
%install

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}
install %{name}-%{version}/*.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/zmi
install %{name}-%{version}/zmi/*.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/zmi

%clean
rm -rf $RPM_BUILD_ROOT

#----------------------------------------------------------------------
%files
%defattr(-,root,root,0755)
%doc LICENSE.txt version.txt

%{_libdir}/zope/lib/python/Products/%{name}/

#----------------------------------------------------------------------
