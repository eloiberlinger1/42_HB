package main

import (
	"bufio"
	"fmt"
	"log/slog"
	"net"
	"os"
)

func main() {

	logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
	slog.SetDefault(logger)

	port := ":4000"
	listener, err := net.Listen("tcp", port)

	if err != nil {
		slog.Error("Server could not start", "error", err)
		os.Exit(1)
	}

	defer listener.Close()

	slog.Info("TCP server started", "port", port)

	for {

		conn, err := listener.Accept()
		if err != nil {
			slog.Warn("Failed to accept connection", "error", err)
			continue
		}

		// Goroutine
		go handleConnection(conn)

	}

}

func handleConnection(conn net.Conn) {

	defer conn.Close()

	remoteAddr := conn.RemoteAddr().String()
	slog.Info("New client connected", "addr", remoteAddr)

	scanner := bufio.NewScanner(conn)

	fmt.Fprintln(conn, "Welcome into TAP server")

	for scanner.Scan() {
		line := scanner.Text()

		slog.Info("Message received", "addr", remoteAddr, "payload", line)
		fmt.Fprintf(conn, "recu: %s\n", remoteAddr)
	}

	slog.Info("Client disconnected", "addr", remoteAddr)

}
