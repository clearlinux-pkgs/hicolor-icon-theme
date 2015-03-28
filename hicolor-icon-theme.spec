#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hicolor-icon-theme
Version  : 0.15
Release  : 3
URL      : http://icon-theme.freedesktop.org/releases/hicolor-icon-theme-0.15.tar.xz
Source0  : http://icon-theme.freedesktop.org/releases/hicolor-icon-theme-0.15.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: hicolor-icon-theme-data

%description
This is the default fallback theme used by implementations of the icon
theme specification.

%package data
Summary: data components for the hicolor-icon-theme package.
Group: Data

%description data
data components for the hicolor-icon-theme package.


%prep
%setup -q -n hicolor-icon-theme-0.15

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/index.theme