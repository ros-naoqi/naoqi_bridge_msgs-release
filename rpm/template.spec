Name:           ros-indigo-naoqi-bridge-msgs
Version:        0.0.6
Release:        0%{?dist}
Summary:        ROS naoqi_bridge_msgs package

Group:          Development/Libraries
License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-genmsg
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-genmsg
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-trajectory-msgs
Conflicts:      ros-indigo-naoqi-msgs
Obsoletes:      ros-indigo-naoqi-msgs

%description
The naoqi_bridge_msgs package provides custom messages for running Aldebaran's
robot such as NAO and Pepper. See the packages nao_robot and pepper_robot for
details.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Nov 08 2016 Karsten Knese <karsten.knese@gmail.com> - 0.0.6-0
- Autogenerated by Bloom

* Sun Nov 15 2015 Karsten Knese <karsten.knese@gmail.com> - 0.0.5-0
- Autogenerated by Bloom

* Mon Nov 09 2015 Karsten Knese <karsten.knese@gmail.com> - 0.0.4-1
- Autogenerated by Bloom

* Wed Aug 26 2015 Karsten Knese <karsten.knese@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Karsten Knese <karsten.knese@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Wed Jun 10 2015 kknese <kknese@todo.todo> - 0.0.2-0
- Autogenerated by Bloom

* Sat May 16 2015 kknese <kknese@todo.todo> - 0.0.1-0
- Autogenerated by Bloom

