/*Once upon a time, on a way through the old wild west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction and coming back the opposite direction is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed the desert the smart way.
The directions given to the man are, for example, the following :

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].

You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]
*/

function dirReduc(arr){
    let x = 0;
    let y = 0;
    let output = []
    for(let i=0;i<arr.length;i++){
        if(arr[i]==="NORTH"){
            y += 1
        }
        if(arr[i]==="SOUTH"){
            y -= 1
        }
        if(arr[i]==="WEST"){
            x -= 1
        }
        if(arr[i]==="EAST"){
            x += 1
        }
    }

    if(y>0){
        for(let i=0;i<y;i++){
            output.push("NORTH")
        }
    }else if(y<0){
        for(let i=0;i>y;i--){
            output.push("SOUTH")
        }
    }
    if(x>0){
        for(let i=0;i<x;i++){
            output.push("EAST")
        }
    }else if(x<0){
        for(let i=0;i>x;i--){
            output.push("WEST")
        }
    }

    return output
}

console.log(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
console.log(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))