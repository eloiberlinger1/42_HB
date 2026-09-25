package main

import (
	"errors"
	"fmt"
)

type Item struct {
	ID          string
	Name        string
	Description string
	Obtainable  bool
}

type Player struct {
	Name      string
	HP        int
	Inventory []*Item
}

func (i *Item) Format() string {
	return fmt.Sprintf("[%s] %s: %s (Can not get item: %t)", i.ID, i.Name, i.Description, i.Obtainable)
}

func (p *Player) AddItem(item *Item) error {
	if item == nil {
		return errors.New("Invalid Item")
	}
	if !item.Obtainable {
		return errors.New("Item not obtainable")
	}
	p.Inventory = append(p.Inventory, item)
	return nil
}

func main() {

	item := &Item{
		ID:          "test",
		Name:        "testname",
		Description: "Old test",
		Obtainable:  true,
	}

	player := &Player{
		Name:      "eloi",
		HP:        9999,
		Inventory: []*Item{},
	}

	err := player.AddItem(item)
	if err != nil {
		fmt.Println("No error occured")
	}

	fmt.Println(item.Format())
}
