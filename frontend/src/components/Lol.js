import React, {Component} from 'react';
import ChampionsLevels from './ChampionsLevels'

class Lol extends Component {

    render() {
        return (
            <div>
                mastery score: {this.props.lol.score}<br/>
                real mastery score: {this.props.lol.realScore}<br/>
                summary mastery points: {this.props.lol.summary_points}<br/>
                <ChampionsLevels champions={this.props.lol} />
                champions not played: {this.props.lol.notPlayedCount} <br/>
                    {this.props.lol.champions.map(function (name,index) {
                        return <div>{index+1} {name}</div>;
                    })}
            </div>
        );
    }
}

export default Lol;