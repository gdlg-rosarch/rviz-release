Name:           ros-indigo-rviz
Version:        1.11.15
Release:        0%{?dist}
Summary:        ROS rviz package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rviz
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp
Requires:       eigen3-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       ogre-devel
Requires:       qt-devel
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-image-geometry
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-interactive-markers
Requires:       ros-indigo-laser-geometry
Requires:       ros-indigo-map-msgs
Requires:       ros-indigo-media-export
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-python-qt-binding
Requires:       ros-indigo-resource-retriever
Requires:       ros-indigo-rosbag
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       ros-indigo-urdf
Requires:       ros-indigo-visualization-msgs
Requires:       tinyxml-devel
Requires:       yaml-cpp-devel
BuildRequires:  assimp-devel
BuildRequires:  eigen3-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ogre-devel
BuildRequires:  qt-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-image-geometry
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-interactive-markers
BuildRequires:  ros-indigo-laser-geometry
BuildRequires:  ros-indigo-map-msgs
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-python-qt-binding
BuildRequires:  ros-indigo-resource-retriever
BuildRequires:  ros-indigo-rosbag
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-urdf
BuildRequires:  ros-indigo-visualization-msgs
BuildRequires:  tinyxml-devel
BuildRequires:  yaml-cpp-devel

%description
3D visualization tool for ROS.

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
* Tue Oct 18 2016 David Gossow <dgossow@gmail.com> - 1.11.15-0
- Autogenerated by Bloom

* Sun Apr 03 2016 David Gossow <dgossow@gmail.com> - 1.11.14-0
- Autogenerated by Bloom

* Wed Mar 23 2016 David Gossow <dgossow@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

* Tue Mar 22 2016 David Gossow <dgossow@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

* Tue Mar 22 2016 David Gossow <dgossow@gmail.com> - 1.11.11-0
- Autogenerated by Bloom

* Tue Oct 13 2015 David Gossow <dgossow@gmail.com> - 1.11.10-0
- Autogenerated by Bloom

* Mon Sep 21 2015 David Gossow <dgossow@gmail.com> - 1.11.9-0
- Autogenerated by Bloom

* Wed Aug 05 2015 David Gossow <dgossow@gmail.com> - 1.11.8-0
- Autogenerated by Bloom

* Mon Mar 02 2015 David Gossow <dgossow@gmail.com> - 1.11.7-0
- Autogenerated by Bloom

* Fri Feb 13 2015 David Gossow <dgossow@gmail.com> - 1.11.6-0
- Autogenerated by Bloom

* Wed Feb 11 2015 David Gossow <dgossow@gmail.com> - 1.11.5-0
- Autogenerated by Bloom

* Thu Oct 30 2014 David Gossow <dgossow@gmail.com> - 1.11.4-0
- Autogenerated by Bloom

* Wed Oct 15 2014 David Gossow <dgossow@gmail.com> - 1.11.3-1
- Autogenerated by Bloom

