import React, { Component } from 'react'
import './css/App.css'
import Box from './components/Box'
const data = require('./data/data.json')

export default class App extends Component {
    render() {
        return (
            <div className="App center">
                <div className="main">
                    <p className="info">총 확진자</p>
                    <h1>{data.all_confirmed_person}</h1>
                    <p className="info">일일 확진자</p>
                    <h1>{data.today_confirmed_person}</h1>
                    <p>누적 입원 환자</p>
                    <h2>{data.all_quarantine_release}</h2>
                    <p>일일 입원 환자</p>
                    <h2>{data.today_quarantine_release}</h2>
                    <p>누적 격리해제</p>
                    <h2>{data.all_cure}</h2>
                    <p>일일 격리해제</p>
                    <h2>{data.today_cure}</h2>
                    <p>누적 사망자</p>
                    <h2>{data.all_die}</h2>
                    <p>일일 사망자</p>
                    <h2>{data.today_die}</h2>
                </div>

                <Box color="white" area="서울" all={10} today={100} />
                <Box color="gray" area="서울" all={10} today={100} />
                <Box color="white" area="서울" all={10} today={100} />
            </div>
        )
    }
}
