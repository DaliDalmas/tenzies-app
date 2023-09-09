import Dice from "../components/dice"
import RollButton from "../components/rollButton"
import React from "react"
import RestartGameButton from "../components/restartGameButton"

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

    const [rollCount, setRollCount] = React.useState(0)

    const [start, setStart] = React.useState(false)

    const [end, setEnd] = React.useState(false)

    function startGame(){
        setStart(true)
        setDiceRolls(()=>{
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
        setRollCount(1)
        setGame({
            selectedNumber: 0,
            play: true
        })
    }

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

        if ((game.play||game.selectedNumber===value)&&(start)){
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

    React.useEffect(()=>(
            setEnd(()=> diceRolls.reduce((total, num)=>num.locked&&total, true))
    ), [diceRolls])
    
    React.useEffect(()=>{
        setStart(false)
    },[end])

    return (
        <div className="app">
            <h1 className="app-title">Tenzies</h1>
            <p className="description">Roll until all dice are the same. Click each die to freeze it at its current value between rolls.</p>
            {end?<div className="roll-count">Game ended with {rollCount} rolls</div>:<div className="roll-count">{rollCount} {rollCount>1? "rolls": "roll"}</div>}
            <Dice diceRolls={diceRolls} lockDie={lockDie}/>
            {!start? <RestartGameButton startGame={startGame}/> : <RollButton roll={roll}/> }
        </div>
    )
}