import Controls from "./Controls";

function RocketDashboard({
    mass, 
    setMass,
    thrust,
    setThrust,
    plotUrl,
    loading,
    onSubmit,
}) {
    return(
        <div className="dashnoard">
            <div className="panel">
                <Controls
                    mass={mass}
                    setMass={setMass}
                    thrust={thrust}
                    setThrust={setThrust}
                    onSubmit={onSubmit}
                />
            </div>
            <div className="panel">
                {loading && <p id="loading">Generating graph...</p>}
                {plotUrl && (
                    <img
                        src={`${plotUrl}?t=${Date.now()}`}
                        alt="Rocket Plot"
                    />
                )}
</div>
        </div>
    );
}
export default RocketDashboard;