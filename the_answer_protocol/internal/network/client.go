package network

import "net"

type Client struct {
	conn net.Conn
	send chan string
	name stirng
}
