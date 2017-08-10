# Generated from tins-1.12.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tins

Name: rubygem-%{gem_name}
Version: 1.12.0
Release: 1%{?dist}
Summary: Useful stuff
Group: Development/Languages
License: MIT
URL: https://github.com/flori/tins
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0
# the following BuildRequires are development dependencies
# BuildRequires: rubygem(gem_hadar) >= 1.7.1
# BuildRequires: rubygem(gem_hadar) < 1.8
# BuildRequires: rubygem(test-unit) >= 3.1
# BuildRequires: rubygem(test-unit) < 4
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
All the stuff that isn't good/big enough for a real library.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/COPYING
%{gem_instdir}/TODO
%{gem_instdir}/VERSION
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/tests
%{gem_instdir}/tins.gemspec

%changelog
* Thu Sep 29 2016 Rich Megginson <rmeggins@redhat.com> - 1.12.0-1
- Initial package
