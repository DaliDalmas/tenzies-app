import Die from "./die"

export default function Dice(props){

    const dice_array = props.diceRolls.map(diceRoll=>(
        <Die
            key={diceRoll.position}
            value={diceRoll.value}
            locked={diceRoll.locked}
            lockDie = {props.lockDie}
            position = {diceRoll.position}/>
            ))
    return (
        <div className="dice">
            {dice_array}
        </div>
    )
}