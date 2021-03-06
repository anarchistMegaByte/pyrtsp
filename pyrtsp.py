#! /usr/bin/python

# pyrtsp - RTSP test server hack
# Copyright (C) 2013  Robert Swain <robert.swain@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import gi
gi.require_version('Gst','1.0')
from gi.repository import GObject, Gst, GstVideo, GstRtspServer

Gst.init(None)


mainloop = GObject.MainLoop()

server = GstRtspServer.RTSPServer()
server.set_address("192.168.5.1")
mounts = server.get_mount_points()

factory = GstRtspServer.RTSPMediaFactory()
factory.set_launch('( autovideosrc device=/dev/video0 is-live=1 ! x264enc speed-preset=ultrafast tune=zerolatency ! rtph264pay name=pay0 pt=96 )')
#factory.set_launch('(v4l2src device=/dev/video0 ! videoconvert ! x264enc)')
mounts.add_factory("/test.mp4", factory)

server.attach(None)

print "stream ready at rtsp://127.0.0.1:8554/test"
mainloop.run()
