# Script generated with Bloom
pkgdesc="ROS - 3D visualization tool for ROS."
url='http://ros.org/wiki/rviz'

pkgname='ros-lunar-rviz'
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
'ros-lunar-catkin'
'ros-lunar-cmake-modules'
'ros-lunar-geometry-msgs'
'ros-lunar-image-transport'
'ros-lunar-interactive-markers'
'ros-lunar-laser-geometry'
'ros-lunar-map-msgs'
'ros-lunar-message-filters'
'ros-lunar-nav-msgs'
'ros-lunar-pluginlib'
'ros-lunar-python-qt-binding'
'ros-lunar-resource-retriever'
'ros-lunar-rosbag'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-roslib'
'ros-lunar-rospy'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf'
'ros-lunar-urdf'
'ros-lunar-visualization-msgs'
'tinyxml'
'urdfdom-headers'
'yaml-cpp'
)

depends=('assimp'
'eigen3'
'mesa'
'ogre-1.9'
'qt5-base'
'ros-lunar-geometry-msgs'
'ros-lunar-image-transport'
'ros-lunar-interactive-markers'
'ros-lunar-laser-geometry'
'ros-lunar-map-msgs'
'ros-lunar-media-export'
'ros-lunar-message-filters'
'ros-lunar-nav-msgs'
'ros-lunar-pluginlib'
'ros-lunar-python-qt-binding'
'ros-lunar-resource-retriever'
'ros-lunar-rosbag'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-roslib'
'ros-lunar-rospy'
'ros-lunar-sensor-msgs'
'ros-lunar-std-msgs'
'ros-lunar-std-srvs'
'ros-lunar-tf'
'ros-lunar-urdf'
'ros-lunar-visualization-msgs'
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
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

