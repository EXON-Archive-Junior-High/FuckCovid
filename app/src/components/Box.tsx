import React, { Component } from 'react'

type boxTypes = {
    color: string,
    area: string,
    all: number,
    today: number
}

export class Box extends Component<boxTypes> {
    render() {
        return (
            <div>
                <div className='box'>
                    <p>{this.props.area}</p>
                    <p>{this.props.all}</p>
                    <p>{this.props.today}</p>
                </div>
            </div>
        )
    }
}

export default Box
