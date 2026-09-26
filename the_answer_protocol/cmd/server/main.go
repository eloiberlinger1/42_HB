package main

import (
	"bufio"
	"fmt"
	"log/slog"
	"net"
	"os"
	"strings"
	"tap-server/internal/network"
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

	hub := network.NewHub()
	go hub.Run()

	for {

		conn, err := listener.Accept()
		if err != nil {
			slog.Warn("Failed to accept connection", "error", err)
			continue
		}

		// Goroutine
		go handleConnection(conn, hub)

	}

}

func handleConnection(conn net.Conn, hub *network.Hub) {

	defer conn.Close()

	remoteAddr := conn.RemoteAddr().String()

	slog.Info("New client connected", "addr", remoteAddr)
	fmt.Fprintln(conn, "S: DK hello proto=1")

	scanner := bufio.NewScanner(conn)
	var username string
	var parts []string
	for {
		if !scanner.Scan() {
			return
		}

		firstLine := scanner.Text()
		parts = strings.Fields(firstLine)

		if len(parts) == 2 && parts[0] == "CONNECT" {
			break
		}

		fmt.Fprintln(conn, "ERR invalid_command")

	}
	username = parts[1]

	client := network.NewClient(conn, username)
	hub.Register(client)
	defer hub.Unregister(client)

	fmt.Fprintln(conn, "S: Connection successful ! \nWelcome %s", username)

	for scanner.Scan() {
		line := scanner.Text()

		slog.Info("Message received", "addr", remoteAddr, "payload", line)
		fmt.Println("\n\n")

		fmt.Print(line)
		fmt.Println("\n\n")

	}

	slog.Info("Client disconnected", "addr", remoteAddr)

}
