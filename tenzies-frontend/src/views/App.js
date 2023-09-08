import Dice from "../components/dice"
import RollButton from "../components/rollButton"
import React from "react"

export default function App(){

    const [diceRolls, setDiceRolls] = React.useState(()=>{
        let startRolls = []
        for(let j=0; j<10; j++){
            startRolls.push({
                position:j+1,
                value: Math.floor(Math.random()*6)+1,
                locked: false
            })
        }
        return startRolls
    })

    const [game, setGame] = React.useState({
        selectedNumber: 0,
        play: true
    })

    const [rollCount, setRollCount] = React.useState(1)

    function roll(){

        setRollCount(oldRollCount=>oldRollCount+1)

        setGame(oldGame=>{
            return {...oldGame, play: true}
        })
        setDiceRolls(prevDiceRolls=>{
            return prevDiceRolls.map(diceRoll=>{
                let inValue;
                inValue = diceRoll.locked? diceRoll.value : Math.floor(Math.random()*6)+1;
                return {...diceRoll, value: inValue}
            })
        })

    }

    function lockDie(position, value){

        if (game.play||game.selectedNumber===value){
            if (game.selectedNumber===value||game.selectedNumber===0){
                setDiceRolls(prevDiceRolls=>{
                    return prevDiceRolls.map(diceRoll=>{
                        return diceRoll.position===position? {...diceRoll, locked:true}: diceRoll
                    })
                })

                
            }
                

            setGame(oldGame=>{
                const valueSelected = oldGame.selectedNumber===0? value : oldGame.selectedNumber
                return {...oldGame, play: false, selectedNumber:valueSelected}
            })
        }
    }

    return (
        <div className="app">
            <h1 className="app-title">Tenzies</h1>
            <p className="description">Roll until all dice are the same. Click each die to freeze it at its current value between rolls.</p>
            <Dice diceRolls={diceRolls} lockDie={lockDie}/>
            <RollButton roll={roll}/>
        </div>
    )
}