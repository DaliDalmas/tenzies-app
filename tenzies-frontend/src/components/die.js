export default function Die(props){
    return (
    <div className={props.locked ? "die locked": "die"} onClick={()=>props.lockDie(props.position, props.value)}>
        {props.value}
    </div>
    )

}