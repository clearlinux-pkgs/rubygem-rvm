#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rvm
Version  : 1.11.3.9
Release  : 4
URL      : https://rubygems.org/downloads/rvm-1.11.3.9.gem
Source0  : https://rubygems.org/downloads/rvm-1.11.3.9.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# rvm
http://rvm.io/
## Description
RVM ~ Ruby Environment Manager ~ Ruby Gem Library

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rvm-1.11.3.9
gem spec %{SOURCE0} -l --ruby > rubygem-rvm.gemspec

%build
gem build rubygem-rvm.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rvm-1.11.3.9.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rvm-1.11.3.9.gem
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/History.md
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/Manifest.yml
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/README.md
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/alias.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/cleanup.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/configuration.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/env.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/gemset.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/info.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/list.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/rubies.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/sets.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/tools.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/utility.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/environment/wrapper.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/install_command_dumper.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/shell.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/shell/abstract_wrapper.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/shell/calculate_rvm_path.sh
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/shell/result.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/shell/shell_wrapper.sh
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/shell/single_shot_wrapper.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/shell/utility.rb
/usr/lib64/ruby/gems/2.3.0/gems/rvm-1.11.3.9/lib/rvm/version.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rvm-1.11.3.9.gemspec
