import React, {Component} from 'react';
import {ProgressBar} from 'react-bootstrap'

class ChampionsLevels extends Component {

    max(a,b){
        if(a>b) return a;
        else return b;
    }


    render() {
        return (
            <div>
                Champion played: <br/>
                {this.props.champions.champion_played.map((name,index) => {
                    return <div>{index+1} {name.name} {name.points}
                    <ProgressBar max={100}>
                        <ProgressBar bsStyle="warning"  now={name.points > 1800  ? 1800 : name.points} key={1} max={21600}/>
                        <ProgressBar bsStyle="success"  now={name.points > 6000  ? 4200 : this.max(name.points - 1800,0)} key={2} max={21600}/>
                        <ProgressBar bsStyle="danger"   now={name.points > 12600 ? 6600 : this.max(name.points - 6000,0)} key={3} max={21600}/>
                        <ProgressBar bsStyle="info"     now={name.points > 21600 ? 9000 : this.max(name.points - 12600,0)} key={4} max={21600}/>
                    </ProgressBar>
                        </div>;
                })}

            </div>
        );
    }
}

export default ChampionsLevels;