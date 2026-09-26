package game

import (
	"fmt"
)

type Item struct {
	ID          string
	Name        string
	Description string
	Obtainable  bool
}

func (i *Item) Format() string {
	return fmt.Sprintf("[%s] %s: %s (Can not get item: %t)", i.ID, i.Name, i.Description, i.Obtainable)
}

// func main() {

// 	item := &Item{
// 		ID:          "test",
// 		Name:        "testname",
// 		Description: "Old test",
// 		Obtainable:  true,
// 	}

// 	player := &Player{
// 		Name:      "eloi",
// 		HP:        9999,
// 		Inventory: []*Item{},
// 	}

// 	err := player.AddItem(item)
// 	if err != nil {
// 		fmt.Println("No error occured")
// 	}

// 	fmt.Println(item.Format())
// }
