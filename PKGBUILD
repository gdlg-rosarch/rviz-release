# Script generated with Bloom
pkgdesc="ROS - 3D visualization tool for ROS."
url='http://ros.org/wiki/rviz'

pkgname='ros-kinetic-rviz'
pkgver='1.12.15_1'
pkgrel=1
arch=('any')
license=('BSD'
'Creative Commons'
)

makedepends=('assimp'
'eigen3'
'mesa'
'ogre-1.9'
'qt5-base'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-interactive-markers'
'ros-kinetic-laser-geometry'
'ros-kinetic-map-msgs'
'ros-kinetic-message-filters'
'ros-kinetic-nav-msgs'
'ros-kinetic-pluginlib'
'ros-kinetic-python-qt-binding'
'ros-kinetic-resource-retriever'
'ros-kinetic-rosbag'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
'tinyxml'
'urdfdom-headers'
'yaml-cpp'
)

depends=('assimp'
'eigen3'
'mesa'
'ogre-1.9'
'qt5-base'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-interactive-markers'
'ros-kinetic-laser-geometry'
'ros-kinetic-map-msgs'
'ros-kinetic-media-export'
'ros-kinetic-message-filters'
'ros-kinetic-nav-msgs'
'ros-kinetic-pluginlib'
'ros-kinetic-python-qt-binding'
'ros-kinetic-resource-retriever'
'ros-kinetic-rosbag'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
'ros-kinetic-urdf'
'ros-kinetic-visualization-msgs'
'tinyxml'
'urdfdom-headers'
'yaml-cpp'
)

conflicts=()
replaces=()

_dir=rviz
source=()
md5sums=()

prepare() {
    cp -R $startdir/rviz $srcdir/rviz
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

