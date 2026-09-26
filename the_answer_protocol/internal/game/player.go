package game

import "errors"

type Player struct {
	Name      string
	HP        int
	Inventory []*Item
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
