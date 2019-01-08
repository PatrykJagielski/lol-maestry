import React, {Component} from 'react';
import ChampionsLevels from './ChampionsLevels'

class Lol extends Component {

    render() {
        return (
            <div>
                <p>mastery score: {this.props.lol.score}</p>
                <p>real mastery score: {this.props.lol.realScore}</p>
                <p>summary mastery points: {this.props.lol.summary_points}</p>
                <ChampionsLevels champions={this.props.lol} />
                <p>champions not played: {this.props.lol.notPlayedCount} <br/>
                    {this.props.lol.champions.map(function (name,index) {
                        return <div>{index+1} {name}</div>;
                    })}</p>
            </div>
        );
    }
}

export default Lol;