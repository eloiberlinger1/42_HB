package network

import "net"

type Client struct {
	conn net.Conn
	send chan string
	name string
}

func NewClient(conn net.Conn, name string) *Client {
	return &Client{
		conn: make(conn conn)
	}
}
