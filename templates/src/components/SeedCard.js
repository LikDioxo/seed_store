import React, {Component} from "react";


class SeedCard extends Component{
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className={"SeedCard"}>
                <div className={"ImagePlacer"}>
                    <a><img src={""}/></a>
                </div>
                <div className={"CardInfo"}/>
                <div className={"CardButton"}>
                    <button>Купить</button>
                </div>
            </div>
        );
    }
}

export default SeedCard