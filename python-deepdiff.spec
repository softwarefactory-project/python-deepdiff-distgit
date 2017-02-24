%global sum     Deep Difference and search of any Python object/data
%global uname   deepdiff

Name:           python-deepdiff
Version:        3.0.0
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/seperman/%{uname}
Source0:        https://github.com/seperman/%{uname}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-numpy
BuildRequires:  python-mock
BuildRequires:  python-nose

%description
Deep Difference of dictionaries, iterables, strings and other objects.
It will recursively look for all the changes.

%package -n python2-deepdiff

Summary:        %sum

%description -n python2-deepdiff
Deep Difference of dictionaries, iterables, strings and other objects.
It will recursively look for all the changes.

%prep
%autosetup -n %{uname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
nosetests -v

%files -n python2-deepdiff
%{python2_sitelib}/

%changelog
* Fri Feb 24 2017 Fabien Boucher <fboucher@redhat.com> - 3.0.0-1
- Initial packaging
