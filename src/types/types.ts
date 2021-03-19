export interface dataInterface{
    todoList: string[],
    handleMinus: (index: number) => void,
    handlePlus: (value: string) => void,
}