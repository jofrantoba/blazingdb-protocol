import abc
import os
import random
import socket
import struct
import threading

__all__ = ['UnixSocketConnection', 'Server', 'Client', 'TcpSocketConnection']


class Buffer(abc.ABC):

  def __len__(self):
    return NotImplemented


Buffer.register(bytes)


class UnixSocketConnection:

  def __init__(self, path):
    self.address_ = path
    self.socket_ = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)

  def __del__(self):
    self.socket_.close()

  def address(self):
    return self.address_

class TcpSocketConnection:

  # ip is the string for the host or regular ip
  # port is an int number
  def __init__(self, ip, port):
    self.ip_ = ip
    self.port_ = port
    self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    server_address = (self.ip_, self.port_)

  def __del__(self):
    self.socket_.close()

  def ip(self):
    return self.ip_

  def port(self):
    return self.port_

  def address(self):
      return (self.ip(), self.port())

class Client:

  def __init__(self, connection):
    self.connection_ = connection
    try:
      connection.socket_.connect(connection.address())
    except socket.error:
      raise RuntimeError("Communication error: connection to " + connection.address() + " was lost")

  def send(self, _buffer):
    try:
      length = struct.pack('I', len(_buffer))
      self.connection_.socket_.sendall(length)
      self.connection_.socket_.sendall(_buffer)
      length = struct.unpack('I', self.connection_.socket_.recv(4))[0]
      return self.connection_.socket_.recv(length)
    except Exception:
      raise RuntimeError("Communication error: when sending data to " + self.connection_.address())
