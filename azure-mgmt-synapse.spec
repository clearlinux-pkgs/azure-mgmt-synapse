#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-mgmt-synapse
Version  : 0.6.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/3a/1a/a8222e7153bd85d9c5bce424dd31e6bdb78d83bf89826c58b3c02fd8987c/azure-mgmt-synapse-0.6.0.zip
Source0  : https://files.pythonhosted.org/packages/3a/1a/a8222e7153bd85d9c5bce424dd31e6bdb78d83bf89826c58b3c02fd8987c/azure-mgmt-synapse-0.6.0.zip
Summary  : Microsoft Azure Synapse Management Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-mgmt-synapse-python = %{version}-%{release}
Requires: azure-mgmt-synapse-python3 = %{version}-%{release}
Requires: azure-common
Requires: azure-mgmt-nspkg
Requires: msrest
Requires: msrestazure
BuildRequires : azure-common
BuildRequires : azure-common~
BuildRequires : azure-mgmt-nspkg
BuildRequires : buildreq-distutils3
BuildRequires : msrest
BuildRequires : msrestazure

%description
This is the Microsoft Azure Synapse Management Client Library.
        This package has been tested with Python 2.7, 3.5, 3.6, 3.7 and 3.8.

%package python
Summary: python components for the azure-mgmt-synapse package.
Group: Default
Requires: azure-mgmt-synapse-python3 = %{version}-%{release}

%description python
python components for the azure-mgmt-synapse package.


%package python3
Summary: python3 components for the azure-mgmt-synapse package.
Group: Default
Requires: python3-core
Provides: pypi(azure_mgmt_synapse)
Requires: pypi(azure_common)
Requires: pypi(msrest)
Requires: pypi(msrestazure)

%description python3
python3 components for the azure-mgmt-synapse package.


%prep
%setup -q -n azure-mgmt-synapse-0.6.0
cd %{_builddir}/azure-mgmt-synapse-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608313175
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
