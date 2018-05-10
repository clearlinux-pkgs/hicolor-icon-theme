#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hicolor-icon-theme
Version  : 0.17
Release  : 11
URL      : http://icon-theme.freedesktop.org/releases/hicolor-icon-theme-0.17.tar.xz
Source0  : http://icon-theme.freedesktop.org/releases/hicolor-icon-theme-0.17.tar.xz
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
%setup -q -n hicolor-icon-theme-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1504184509
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1504184509
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/index.theme
