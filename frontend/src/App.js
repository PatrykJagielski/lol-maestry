import React, { Component } from 'react';

class App extends Component {
    constructor(){
        super()
        this.state = {
            summonerName: "",
            summonerID: "",
            isPlaying: false,
            champions: [],
            notPlayedCount: 0,
            score: 0,
            realScore: 0,
            rotationChampions: [],
            champion_points: [],
            chest_granted: [],
            champion_levels: [],
            champion_points_since_last_level: [],
            champion_points_until_next_level: [],
            summary_points: 0
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleChange(event){
        const {name, value} = event.target
        this.setState({
            [name]: value
        })
    }

    handleSubmit(event){
        event.stopPropagation()
        const url = 'http://localhost:5000/summoner/eun1/' + this.state.summonerName
        fetch(url)
            .then(response => response.json())
            // .then(parsedJSON => console.log(parsedJSON))
            .then(parsedJSON => {
                return this.setState({
                    score: parsedJSON["score"],
                    realScore: parsedJSON["real_score"],
                    summonerID: parsedJSON["id"],
                    isPlaying: parsedJSON["is_playing"],
                    notPlayedCount: parsedJSON["not_played_count"],
                    rotationChampions: parsedJSON["rotation_champions_not_played"],
                    champions: parsedJSON["champions"],
                    champion_points: parsedJSON["champion_points"],
                    chest_granted: parsedJSON["chest_granted"],
                    champion_levels: parsedJSON["champion_levels"],
                    champion_points_since_last_level: parsedJSON["champion_points_since_last_level"],
                    champion_points_until_next_level: parsedJSON["champion_points_until_next_level"],
                    summary_points: parsedJSON["summary_points"]
                });
            })
            .catch(error => console.log(error))
        event.preventDefault()
    }

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <input
                        name="summonerName"
                        value={this.state.summonerName}
                        onChange={this.handleChange}
                        placeholder="Summoner Name"
                    />
                    <input type="submit" value="Submit" />
                </form>

                <br />
                <p>maesrty score: {this.state.score}</p>
                <p>real maestry score: {this.state.realScore}</p>
                <p>summary maestry points: {this.state.summary_points}</p>
                <p>champions not played: {this.state.notPlayedCount} <br/>
                    {this.state.champions.map(function (name,index) {
                        return <div>{index+1} {name}</div>;
                    })}</p>
            </div>
        );
    }
}

export default App;
