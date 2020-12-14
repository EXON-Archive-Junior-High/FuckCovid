import React, { Component } from 'react'

type boxTypes = {
    area: string,
    all: number,
    today: number
}

export class Box extends Component<boxTypes> {

    render() {
        return (
            <div className="box">
                <p>{this.props.area}</p>
                <p>{this.props.all}</p>
                <p>{this.props.today}</p>
            </div>
        )
    }
}

export default Box
